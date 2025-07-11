# Set pandoc path
Sys.setenv(RSTUDIO_PANDOC = "/usr/bin")

# Check pandoc availability
cat("Checking pandoc availability...\n")
cat("Pandoc available:", rmarkdown::pandoc_available(), "\n")
cat("Pandoc version:", as.character(rmarkdown::pandoc_version()), "\n")

# Render the presentation
cat("Rendering presentation...\n")
rmarkdown::render(
  "shiny-introduction.Rmd",
  output_format = revealjs::revealjs_presentation(
    theme = "default",
    css = "custom.css",
    highlight = "pygments",
    center = TRUE,
    transition = "slide",
    self_contained = FALSE,
    slide_level = 2,
    reveal_options = list(
      controls = TRUE,
      progress = TRUE,
      history = TRUE,
      keyboard = TRUE,
      overview = TRUE,
      touch = TRUE,
      loop = FALSE,
      rtl = FALSE,
      shuffle = FALSE,
      fragments = TRUE,
      embedded = FALSE,
      help = TRUE,
      showNotes = FALSE,
      autoSlide = 0,
      autoSlideStoppable = TRUE,
      mouseWheel = FALSE,
      hideAddressBar = TRUE,
      previewLinks = FALSE,
      transition = "slide",
      transitionSpeed = "default",
      backgroundTransition = "fade"
    )
  )
)

cat("Rendering completed!\n") 