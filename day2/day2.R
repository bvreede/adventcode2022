library(tidyverse)

input <- readr::read_table("day2/input.txt", col_names = FALSE) |>
  mutate(
  Elf = case_when(
    X1 == "A" ~ "Rock",
    X1 == "B" ~ "Paper",
    X1 == "C" ~ "Scissors"),
  You = case_when(
    X2 == "X" ~ "Rock",
    X2 == "Y" ~ "Paper",
    X2 == "Z" ~ "Scissors"),
  Value = case_when(
    You == "Rock" ~ 1,
    You == "Paper" ~ 2,
    You == "Scissors" ~ 3),
  Game = case_when(
    You == Elf ~ 3,
    Elf == "Paper" & You == "Scissors" ~ 6,
    Elf == "Paper" & You == "Rock" ~ 0,
    Elf == "Rock" & You == "Paper" ~ 6,
    Elf == "Rock" & You == "Scissors" ~ 0,
    Elf == "Scissors" & You == "Rock" ~ 6,
    Elf == "Scissors" & You == "Paper" ~ 0),
  Total = Value + Game
  )

# total score
sum(input$Total)

# part 2
input <- input |>
  mutate(
    Game2 = case_when(
      X2 == "X" ~ 0,
      X2 == "Y" ~ 3,
      X2 == "Z" ~ 6),
    You2 = case_when(
      Game2 == 3 ~ Elf,
      Game2 == 0 & Elf == "Paper" ~ "Rock",
      Game2 == 0 & Elf == "Rock" ~ "Scissors",
      Game2 == 0 & Elf == "Scissors" ~ "Paper",
      Game2 == 6 & Elf == "Rock" ~ "Paper",
      Game2 == 6 & Elf == "Scissors" ~ "Rock",
      Game2 == 6 & Elf == "Paper" ~ "Scissors"),
    Value2 = case_when(
      You2 == "Rock" ~ 1,
      You2 == "Paper" ~ 2,
      You2 == "Scissors" ~ 3),
    Total2 = Value2 + Game2
  )
sum(input$Total2)
