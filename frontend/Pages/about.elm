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
    Grid.container []
        [ CDN.stylesheet
        , Grid.row
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/github.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Github"] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/pivotaltracker.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Pivotal Tracker" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/cassandra.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Cassandra" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/storm.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Storm" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/maven.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Maven" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/aws.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "AWS" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/twitter.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Twitter" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/json.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "JSON" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/python.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Python" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/textblob.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "TextBlob" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/django.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Django" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/gmaps.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Google Maps" ] ]
            ]
        , Grid.row 
            [ Row.middleXs
            , Row.centerMd
            , Row.leftSm
            , Row.attrs [ style [("margin-top", "30px")] ]
            ]
            [ Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/Elm.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "Elm" ] ]
            , Grid.col [ Col.sm2 ] 
                [ img 
                    [ src "../images/html.png"
                    , style [ ( "width", "75px" ) ] 
                    ] 
                    [] 
                ]
            , Grid.col [ Col.sm4 ] [ h6 [] [ text "HTML" ] ]
            ]
        ]
{-    navbar DefaultNavbar 
        [ style 
            [("color", "gray")]
        ]
        [ h1 [][text "Tweet Dat(a) Hate"]
        ]
    div 
        []
        [ div [] [text "Tweet Dat(a) Hate"]
        , div [] []
        ]
    div
        []
        [
        ] -}


-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none

-- INIT 
init: (Model, Cmd Msg)
init = 
    (Model "Tweet Dat(a) Hate" "", Cmd.none)

