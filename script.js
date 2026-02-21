const emojiMap = {
  rock: "✊",
  paper: "👋",
  scissors: "✌️",
};

let playerScore = 0;
let computerScore = 0;
let isMuted = false;

const choiceButtons = document.querySelectorAll(".choice-btn");
const resetBtn = document.getElementById("resetBtn");
const muteBtn = document.getElementById("muteBtn");
const bgAudio = document.getElementById("bgAudio");

const playerScoreDisplay = document.getElementById("playerScore");
const computerScoreDisplay = document.getElementById("computerScore");
const playerEmojiDisplay = document.getElementById("playerEmoji");
const computerEmojiDisplay = document.getElementById("computerEmoji");
const playerChoiceDisplay = document.getElementById("playerChoice");
const computerChoiceDisplay = document.getElementById("computerChoice");
const resultDisplay = document.getElementById("resultText");
const resultContainer = document.querySelector(".result");

// Audio control
muteBtn.addEventListener("click", () => {
  isMuted = !isMuted;
  if (isMuted) {
    bgAudio.pause();
    muteBtn.textContent = "🔇 Unmute";
    muteBtn.classList.add("muted");
  } else {
    bgAudio.play();
    muteBtn.textContent = "🔊 Mute";
    muteBtn.classList.remove("muted");
  }
});

function getComputerChoice() {
  const choices = ["rock", "paper", "scissors"];
  return choices[Math.floor(Math.random() * choices.length)];
}

function determineWinner(userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return "Draw!";
  }

  if (
    (userChoice === "rock" && computerChoice === "scissors") ||
    (userChoice === "scissors" && computerChoice === "paper") ||
    (userChoice === "paper" && computerChoice === "rock")
  ) {
    return "You win!";
  }

  return "You lose!";
}

function playGame(playerChoice) {
  const computerChoice = getComputerChoice();
  const result = determineWinner(playerChoice, computerChoice);

  // Display choices
  playerEmojiDisplay.textContent = emojiMap[playerChoice];
  playerChoiceDisplay.textContent = playerChoice;

  computerEmojiDisplay.textContent = emojiMap[computerChoice];
  computerChoiceDisplay.textContent = computerChoice;

  // Display result
  resultDisplay.textContent = result;
  resultContainer.className = "result";

  if (result === "You win!") {
    playerScore++;
    resultContainer.classList.add("win");
  } else if (result === "You lose!") {
    computerScore++;
    resultContainer.classList.add("lose");
  } else {
    resultContainer.classList.add("draw");
  }

  // Update scores
  playerScoreDisplay.textContent = playerScore;
  computerScoreDisplay.textContent = computerScore;
}

function resetGame() {
  playerScore = 0;
  computerScore = 0;
  playerScoreDisplay.textContent = "0";
  computerScoreDisplay.textContent = "0";
  playerEmojiDisplay.textContent = "-";
  computerEmojiDisplay.textContent = "-";
  playerChoiceDisplay.textContent = "-";
  computerChoiceDisplay.textContent = "-";
  resultDisplay.textContent = "Make your move!";
  resultContainer.className = "result";
}

choiceButtons.forEach((button) => {
  button.addEventListener("click", (e) => {
    const choice = e.target.dataset.choice;
    playGame(choice);
  });
});

resetBtn.addEventListener("click", resetGame);
