module About exposing (..)

import Bootstrap.Navbar exposing (..)

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
view: Model -> Html Msg
view model = 
    navbar DefaultNavbar 
        [ style 
            [("color", "gray")]
        ]
        [ h1 [][text "Tweet Dat(a) Hate"]
        ]
{-    div 
        []
        [ div [] [text "Tweet Dat(a) Hate"]
        , div [] []
        ]
    div
        []
        [
        ]-}


-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none

-- INIT 
init: (Model, Cmd Msg)
init = 
    (Model "Tweet Dat(a) Hate", Cmd.none)

