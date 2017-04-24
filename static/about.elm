module Pages.About exposing (..)

import Bootstrap.CDN as CDN
import Bootstrap.Navbar exposing (..)
import Bootstrap.Grid as Grid
import Bootstrap.Grid.Col as Col
import Bootstrap.Grid.Row as Row
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

main = 
    Html.program 
        { init = init
        , view = view
        , update = update
        , subscriptions = subscriptions
        }

-- MODEL
type alias Model = 
    { tech: String
    , image: String
    }


-- UPDATE 
type Msg = 
    Title
    | Header String

update: Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of 
        Title -> 
            (Model "Tweet Dat(a) Hate" "", Cmd.none)
        Header newHeader ->
            (Model newHeader "", Cmd.none)


-- VIEW 
view: model -> Html Msg
view model = 
    Grid.container 
        [style 
            [ ("padding-left", "15px")
            , ("padding-right", "45px")
            , ("margin-left", "15px")
            , ("margin-right", "15px")]
        ]
        [ CDN.stylesheet
        , Grid.row
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/github.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Github"]
                , text "We used GitHub as our main code repository for version control." 
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/pivotaltracker.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Pivotal Tracker" ] 
                , text "Pivotal Tracker served as our project management tool in an Agile environment." 
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/cassandra.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Cassandra" ] 
                , text "Cassandra stored the tweet data after filtering."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/storm.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Storm" ] 
                , text "Storm handled the queuing of our Twitter API data stream and also handled the processing of the data stream."
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/maven.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Maven" ] 
                , text "Maven compiled our Cassandra database and our Storm package."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/aws.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "AWS" ] 
                , text "AWS hosted the servers for all of our components."
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/twitter.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Twitter" ] 
                , text "Using Twitter's API, we pulled tweets to filter for hateful sentiment across the country."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/json.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "JSON" ] 
                , text "JSON lets us transfer data easily in a standard data structure."
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/python.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Python" ] 
                , text "We used Python everywhere. Our sentiment analysis and its Storm bolt is in Storm, and we used Python to talk to the database. Our front-end web-server also uses Python."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/textblob.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "TextBlob" ] 
                , text "TextBlob, a Python library, allows us to do sentiment analysis on the content of tweets."
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/django.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Django" ] 
                , text "Django Unchained. 'Nuff said."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/gmaps.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Google Maps" ] 
                , text "Google Maps API allowed us to determine the location of each tweet in order to map it to a state in Cassandra."
                ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/Elm.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "Elm" ] 
                , text "We used Elm in conjunction with HTMl, JavaScript, and CSS to create the webpage."
                ]
            , Grid.col [ Col.sm2, Col.attrs [ class "tech-img" ] ] 
                [ img 
                    [ src "../images/html.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4, Col.attrs [ class "tech-desc" ] ] 
                [ h6 [] [ text "HTML" ] 
                , text "We used HTML in conjunction with Elm, JavaScript, and CSS to create the webpage."
                ]
            ]
        ]


-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none

-- INIT 
init: (Model, Cmd Msg)
init = 
    (Model "Tweet Dat(a) Hate" "", Cmd.none)

