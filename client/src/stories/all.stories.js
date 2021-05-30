import React from "react";
import { storiesOf } from "@storybook/react";
import { action, withActions } from "@storybook/addon-actions";
import { addDecorator } from "@storybook/react";
import { GlobalStyle } from "../fonts";
import {
  LetterButton,
  ButtonPanel,
  StartForm,
  PlayAgainPanel,
} from "../buttons";
import { Banner, ResultBanner, UsageAndBlanks } from "../components";

addDecorator((s) => (
  <>
    <GlobalStyle />
    {s()}
  </>
));

storiesOf("Button-related Components", module)
  .add("LetterButton", () => (
    <div>
      <h2>LetterButton(letter, wasUsed, makeGuess)</h2>
      <ul>
        <li>letter - the button text, assumed to be one character</li>
        <li>
          wasUsed - (Boolean) whether the button was used; affects styling
        </li>
        <li>makeGuess - callBack to use on button click</li>
      </ul>
      <h3>Already used</h3>
      <LetterButton letter="A" wasUsed={true} makeGuess={action("click-A")} />
      <h3>Not yet used</h3>
      <LetterButton letter="B" wasUsed={false} makeGuess={action("click-B")} />
    </div>
  ))

  .add("ButtonPanel", () => (
    <div>
      <h2>ButtonPanel(language, onGuess)</h2>
      <ul>
        <li>onGuess - a callback that takes the guessed letter</li>
        <li>usedLetters - a string of already-guessed letter</li>
      </ul>
      <h3>Used Letters rlstine</h3>
      <ButtonPanel onGuess={action("guessed")} usedLetters="rlstine" />
      <h3>Used Letters senorita</h3>
      <ButtonPanel onGuess={action("guessed")} usedLetters="senorita" />
      <h3>Used Letters mondieu</h3>
      <ButtonPanel onGuess={action("guessed")} usedLetters="mondieu" />
    </div>
  ))

  .add("StartForm", () => (
    <div>
      <h2>StartForm(clickStart)</h2>
      <ul>
        <li>ClickStart - game starting callback, takes name and language</li>
      </ul>
      <StartForm clickStart={action("start-game")} />
    </div>
  ))

  .add("PlayAgainPanel", () => (
    <div>
      <h2>PlayAgainPanel(lang, clickPlayAgain)</h2>
      <ul>
        <li>lang - the language in which the last game was played</li>
        <li>clickPlayAgain - callback talking the new language choice</li>
        <li>clickQuit - callback to quit playing</li>
      </ul>
      <h3>Default English</h3>
      <PlayAgainPanel
        lang="en"
        clickPlayAgain={action("play-again")}
        clickQuit={action("quit-game")}
      />
      <h3>Default French</h3>
      <PlayAgainPanel
        lang="fr"
        clickPlayAgain={action("play-again")}
        clickQuit={action("quit-game")}
      />
    </div>
  ));

storiesOf("Banners and Displays", module)
  .add("Banner", () => (
    <div>
      <h2>Banner(full)</h2>
      <p>
        This component includes both Banner and ShortTitle from the design docs.
      </p>
      <ul>
        <li>
          full - truthy means wide title is shown with subtitle, otherwise shows
          just short title
        </li>
      </ul>
      <h3>Full Title</h3>
      <Banner full={true} />
      <h3>Short Title</h3>
      <Banner full={false} />
    </div>
  ))
  .add("ResultBanner", () => (
      <div>
          <h2>ResultBanner(winResult)</h2>
          <ul>
              <li>winResult - truthy means the player won, otherwise the player lost</li>
          </ul>
          <h3>Player won the game</h3>
          <ResultBanner winResult={true}/>
          <h3>Player lost the game</h3>
          <ResultBanner/>
      </div>
  ))
  .add("UsageAndBlanks", () => (
      <div>
          <h2>UsageAndBlanks(usage, blanks, showBlanks)</h2>
          <p>This component uses the non-React function prepareUsage.</p>
          <ul>
              <li>
                  usage - usage example with guess word as underscores
              </li>
              <li>blanks - guessed/non-guessed letters, like "h_ml_t"</li>
              <li>showBlanks - whether to show blanks separately or in usage</li>
          </ul>
          <h3>With blanks</h3>
          <UsageAndBlanks
          usage="The sky loomed dark and ______."
          blanks="__oo_y"
          showBlanks={true}
          />
          <UsageAndBlanks
          usage="The sky loomed dark and ______."
          blanks="gloomy"
          showBlanks={false}
          />
      </div>
  ));