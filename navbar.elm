--module Base.Navbar exposing (..)

import Bootstrap.Navbar as Navbar
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

type alias Model = 
    { navbarState : Navbar.State }

initState : (Model, Cmd Msg)
initState toMsg = 
    let
        (navbarState, navbarCmd) = 
            Navbar.initialState NavbarMsg
    in 
        ({ navbarState = navbarState }, navbarCmd )

type Msg = NavbarMsg Navbar.State

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of 
        NavbarMsg state ->
            ( { model | navbarState = state }, Cmd.none)

view : Model -> Html Msg
view model = 
    Navbar.config NavbarMsg
        |> Navbar.withAnimation
        |> Navbar.brand 
            [ href "#" ] 
            [ text "Tweet Dat(a) Hate" ]
        |> Navbar.view model.navbarState