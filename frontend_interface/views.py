# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic.base import TemplateView

from cassandra.cluster import Cluster
from cassandra.query import *

import json
import time
import re
# Create your views here.

def mapsData(request):
	'''
	statesToInsert=['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'newhampshire', 'newjersey', 'newmexico', 'newyork', 'northcarolina', 'northdakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania', 'rhodeisland', 'southcarolina', 'southdakota', 'tennessee', 'texas', 'utah', 'vermont', 'virginia', 'washington', 'westvirginia', 'wisconsin', 'wyoming']
	stateToCode = {"alabama":"Alabama","alaska":"Alaska","arizona":"Arizona","arkansas":"Arkansas","california":"California","colorado":"Colorado","connecticut":"Connecticut","delaware":"Delaware","florida":"Florida","georgia":"Georgia","hawaii":"Hawaii","idaho":"Idaho","illinois":"Illinois","indiana":"Indiana","iowa":"Iowa","kansas":"Kansas","kentucky":"Kentucky","louisiana":"Louisiana","maine":"Maine","maryland":"Maryland","massachusetts":"Massachusetts","michigan":"Michigan","minnesota":"Minnesota","mississippi":"Mississippi","missouri":"Missouri","montana":"Montana","nebraska":"Nebraska","nevada":"Nevada","newhampshire":"New Hampshire","newjersey":"New Jersey","newmexico":"New Mexico","newyork":"New York","northcarolina":"North Carolina","northdakota":"North Dakota","ohio":"Ohio","oklahoma":"Oklahoma","oregon":"Oregon","pennsylvania":"Pennsylvania","rhodeisland":"Rhode Island","southcarolina":"South Carolina","southdakota":"South Dakota","tennessee":"Tennessee","texas":"Texas","utah":"Utah","vermont":"Vermont","virginia":"Virginia","washington":"Washington","westvirginia":"West Virginia","wisconsin":"Wisconsin","wyoming":"Wyoming"}
	resultSet = []
	resultSet.append(["State", "Hate Score"])
	for state in statesToInsert:
		stateValue = stateDataQuery(state)
		result = stateValue['results']['percent']['percent']
		resultSet.append([stateToCode[state],result])
	'''
	returnValue = {}
	returnValue['values'] = mapSetQuery()
	'''
	returnValue = {}
	returnValue['values'] = resultSet
	response = HttpResponse()
	'''
	response.write(json.dumps(returnValue))
	return response

def stateData(request, statename):
	response = HttpResponse()
	try:
		statename = re.sub("[^a-zA-Z]", "", statename).lower()
		response.write(json.dumps(stateDataQuery(statename)))
	except:
		response.write("No available data for: %s" % statename)

	return response


class HomePageView(TemplateView):
    template_name = 'ilbdaicl/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'hello http://example.com')
        return context

class TeamPageView(TemplateView):
    template_name = 'ilbdaicl/team.html'

    def get_context_data(self, **kwargs):
        context = super(TeamPageView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'hello http://example.com')
        return context

class TechnologiesPageView(TemplateView):
    template_name = 'ilbdaicl/technologies.html'

    def get_context_data(self, **kwargs):
        context = super(TechnologiesPageView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'hello http://example.com')
        return context

class AnalyticsPageView(TemplateView):
    template_name = 'ilbdaicl/analytics.html'

    def get_context_data(self, **kwargs):
        context = super(AnalyticsPageView, self).get_context_data(**kwargs)
        #messages.info(self.request, 'hello http://example.com')
        return context

def stateDataQuery(statename):
	cluster = Cluster(['172.31.3.194'], port=9042)
	session = cluster.connect()
	current = str(date.today())
	epoch = int(time.mktime(time.strptime(current, '%Y-%m-%d')))*1000
	week = 604800000
	daily = 86400000
	week = daily*7
	lowerEnd = epoch - week
	state = statename
	session.execute("USE twittertweets;")
	values = []
	history = dict()
	percent = dict()
	while ((lowerEnd+daily) != epoch):
		day = lowerEnd + daily
		hate = session.execute("select count(*) from "+state+" where time>="+str(lowerEnd)+" and time<="+str(day)+" and sentimentscore>0 allow filtering;")[0]
		hate = str(hate).split('=')
		hate = hate[1]
		hate = hate.replace(")","")
		neutral = session.execute("select count(*) from "+state+" where time>="+str(lowerEnd)+" and time<="+str(day)+" and sentimentscore=0 allow filtering;")[0]
		neutral = str(neutral).split('=')
		neutral = neutral[1]
		neutral = neutral.replace(")","")
		total = float(hate) + float(neutral)
		if total != 0:
			percentage = float(float(hate)/float(total)*100)
			values.append((hate, int(total), percentage))
			history[day] = percentage
		else:
			values.append((0,0,0))
			history[day] = 0
		lowerEnd += daily
		firstSet = values[0]
	        
        	percent['hate'] = firstSet[0]
	        percent['nonhate'] = firstSet[1]
        	percent['percent'] = firstSet[2]
		
        hate = session.execute("select count(*) from "+state+" where time>="+str(lowerEnd)+" and time<="+str(epoch)+" and sentimentscore>0 allow filtering;")[0]
        hate = str(hate).split('=')
        hate = hate[1]
        hate = hate.replace(")","")
        neutral = session.execute("select count(*) from "+state+" where time>="+str(lowerEnd)+" and time<="+str(epoch)+" and sentimentscore=0 allow filtering;")[0]
        neutral = str(neutral).split('=')
        neutral = neutral[1]
        neutral = neutral.replace(")","")
        total = float(hate) + float(neutral)
        if total != 0:
                percentage = float(float(hate)/float(total)*100)
                values.append((hate, int(total), percentage))
                history[day] = percentage
        else:
	          values.append((0,0,0))
                  history[day] = 0
	firstSet = values[len(values)-1]
	percent['hate'] = firstSet[0]
	percent['nonhate'] = firstSet[1]
	percent['percent'] = firstSet[2]

	finalValue = { "results": { "history": history, "percent": percent}}
	return finalValue

def mapSetQuery():
	cluster = Cluster(['172.31.3.194'], port=9042)
	session = cluster.connect()
	statesToInsert = {
	'Arkansas',
	'Alabama',
	'Arizona',
	'Alaska',
	'California',
	'Colorado',
	'Connecticut',
	'Delaware',
	'Florida',
	'Georgia',
	'Hawaii',
	'Iowa',
	'Idaho',
	'Illinois',
	'Indiana',
	'Kansas',
	'Kentucky',
	'Louisiana',
	'Massachusetts',
	'Maryland',
	'Maine',
	'Michigan',
	'Minnesota',
	'Missouri',
	'Mississippi',
	'Montana',
	'NorthCarolina',
	'NorthDakota',
	'Nebraska',
	'NewHampshire',
	'NewJersey',
	'NewMexico',
	'Nevada',
	'NewYork',
	'Ohio',
	'Oklahoma',
	'Oregon',
	'Pennsylvania',
	'RhodeIsland',
	'SouthCarolina',
	'SouthDakota',
	'Tennessee',
	'Texas',
	'Utah',
	'Virginia',
	'Vermont',
	'Washington',
	'Wisconsin',
	'WestVirginia',
	'Wyoming'
	}

	session.execute("USE twittertweets;")
	count = 0
	returnValues = dict()
	totals = []
	totals.append(["State", "Hate Score"])
	for item in statesToInsert:
	#Insert Tables
	        neutral = session.execute("select count(*) from "+item+" where sentimentscore=0 allow filtering;")[0]
	        neutral = str(neutral).split('=')
	        neutral = neutral[1]
	        neutral = neutral.replace(")","")
	        #print(item+" sentiment=0 count="+StateCount)
	        hate = session.execute("select count(*) from "+item+" where sentimentscore>0 allow filtering;")[0]
	        hate = str(hate).split('=')
	        hate = hate[1]
	        hate = hate.replace(")","")
	        total = int(neutral) + int(hate)
	        percentage = float((float(hate)/float(total))*100)
	        totals.append([item,percentage])
	        #print(item+" Hate Percentage: {}% Total: {}".format(float((float(hate)/float(total))*100),total))
	returnValues['values'] = totals
	cluster.shutdown()