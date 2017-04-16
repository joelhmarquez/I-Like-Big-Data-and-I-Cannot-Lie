module About exposing (..)

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
    { topic: String
    }


-- UPDATE 
type Msg = 
    Title
    | Header String

update: Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of 
        Title -> 
            (Model "Tweet Dat(a) Hate", Cmd.none)
        Header newHeader ->
            (Model newHeader, Cmd.none)


-- VIEW 
view: model -> Html Msg
view model = 
    Grid.container []
        [ Grid.row
            [ Row.topXs
            , Row.centerMd
            , Row.leftSm
            ]
            [ Grid.col [ Col.xl9 ] [ text "Tech 1" ]
            , Grid.col [ Col.xs1 ] [ text "Tech 2" ]
            ]
        , Grid.row 
            [ Row.topXs
            , Row.centerMd
            , Row.leftSm
            ]
            [ Grid.col [] [ text "Tech 3" ]
            , Grid.col [] [ text "Tech 4" ]
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
    (Model "Tweet Dat(a) Hate", Cmd.none)

