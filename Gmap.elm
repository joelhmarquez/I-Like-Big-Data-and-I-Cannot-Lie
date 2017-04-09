{-
Attempting to use Elm to update Google Maps, based on tutorial: 
    https://github.com/simonh1000/elm-google-maps-2/blob/master/src/Main.elm
    http://simonh1000.github.io/2015/10/elm-architecture-ports/
-}

port module Gmap exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing(..)
import Json.Encode as E exposing (Value)
import Time exposing (Time)
import Task exposing (..)

main = 
    Html.program 
        { init = init
        , view = view
        , update = update
        , subscriptions = always (receiveMap JSMap)
        }

-- MODEL
type alias LatLng = 
    { lat : Float
    , lng : Float
    }

type Action = 
    MapLoaded
    | MapError

type alias Model = 
    { gmap : Value
    , center : LatLng
    }

-- UPDATE 
type Msg = 
    Shift
    | Tick Time
    | JSMap Value

update: Msg -> Model -> ( Model, Cmd Msg )
update message model = 
    case message of
        Shift ->
            let
                center = model.center
                newCenter = 
                    { center | lat = center.lat+1 }
                newModel = 
                    { model | center = newCenter }
            in
                newModel ! [ setCenter newModel ]
        JSMap gmap ->
            { model | gmap = gmap } ! []
        Tick _ ->
            model ! [loadMap model.center]

-- VIEW 
view : Model -> Html Msg
view model =
    div
        [ style
            [ ( "display", "flex" ) ]
        ]
        [ div []
            [ h3 [] [ text "" ]
            , button
                [ onClick Shift ]
                [ text "Shift Map"]
            ]
        , div []
            [ h3[] [ text "Map Display" ]
            , gmap [ mapDisplay ] []
            ]
        ]

mapDisplay : Attribute msg 
mapDisplay = 
    style 
        [ ("display", "block" )
        , ( "height", "300px" )
        , ( "width", "500px")
        ]

gmap : List (Attribute msg) -> List (Html msg) -> Html msg
gmap = 
    node "gmap"

-- PORTS
port loadMap : LatLng -> Cmd msg

port setCenter : Model -> Cmd msg

port receiveMap : (Value -> msg) -> Sub msg

-- INIT 

init : (Model, Cmd Msg)
init = 
    let init_point =
        LatLng 39.7 105
    in 
        ( Model (E.string "filler") init_point
        , Time.now |> Task.perform Tick
        )