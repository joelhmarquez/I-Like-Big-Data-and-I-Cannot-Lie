{- Simple page that has counter buttons.
Following the elm-lang tutorial:
https://guide.elm-lang.org/architecture/user_input/buttons.html

This project includes the extension excercise to have a "Reset" button.
-}

import Html exposing(Html, button, div, text)
import Html.Events exposing (onClick)

main =
 Html.beginnerProgram{ model = model, view = view, update = update}


-- MODEL

type alias Model = Int

model : Model
model =
 0


-- UPDATE

type Msg = Increment | Decrement | Reset

update : Msg -> Model -> Model
update msg model =
 case msg of
  Increment ->
   model + 1

  Decrement ->
   model - 1

  Reset ->
   0


-- VIEW

view : Model -> Html Msg
view model = 
 div []
  [button[onClick Decrement][text "-"]
  , div[] [text (toString model)]
  , button [onClick Increment][text "+"]
  , div[][]
  , button [onClick Reset][text "Reset"]
  ]
