module Base.Navbar exposing (..)

import Bootstrap.CDN as CDN
import Bootstrap.Navbar as Navbar
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)

-- MAIN
main = 
    Html.program
        { view = view
        , update = update
        , subscriptions = subscriptions
        , init = initState}

-- MODEL
type alias Model = 
    { navbarState : Navbar.State }

-- INIT
initState : (Model, Cmd Msg)
initState = 
    let
        (navbarState, navbarCmd) = 
            Navbar.initialState NavbarMsg
    in 
        ({ navbarState = navbarState }, navbarCmd )

-- UPDATE
type Msg = NavbarMsg Navbar.State

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of 
        NavbarMsg state ->
            ( { model | navbarState = state }, Cmd.none)

-- SUBSCRIPTIONS
subscriptions : Model -> Sub Msg
subscriptions model = 
    Navbar.subscriptions model.navbarState NavbarMsg


-- VIEW
view : Model -> Html Msg
view model = 
    Navbar.config NavbarMsg
        |> Navbar.fixTop
        |> Navbar.collapseLarge
        -- |> Navbar.withAnimation
        |> Navbar.brand 
            [ href "#"
            , style [("color", "gray")]
            ] 
            [ CDN.stylesheet
            , h1 [] [text "Tweet Dat(a) Hate" ]]
        |> Navbar.items
            [ Navbar.itemLink [href "#"] [ text "Visualize" ]
            , Navbar.itemLink [href "#"] [ text "About" ]
            ]
        |> Navbar.view model.navbarState