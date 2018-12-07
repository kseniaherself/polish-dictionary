library(tidyverse); library(rvest); library('xml2'); library(stringr); library(foreach); library(beepr); 
#library(doParallel)

results <- data.frame(id = numeric(), wordform = character(), url = numeric())

urls <- paste0("http://sgjp.pl/edycja/ajax/inflection-tables/?lexeme_id=",
               1:5000, #9999999,
               "&variant=1")

if(TRUE){
  sapply(1:5000, function(url_n){ #999999, function(url_n){
  print(url_n)
  html <- jsonlite::fromJSON(urls[url_n])$html
  if(!is.null(html)){
  source <- read_html(html)
  tag <- unlist(str_extract_all(str_extract(source, 'span class="form p.*?"'), "p[0-9]{1,}"))
  if (tag != "NULL") {
    sapply(1:length(tag), function(id){
    source %>% 
      #html_nodes(css = "td") %>%
      html_nodes(css = paste0("span.form.", tag[id])) %>%
      html_text() ->
        result
      results <<- rbind(results, data.frame(id = url_n, wordform = result, url = urls[url_n]))
    })}} else{
      results <<- rbind(results, data.frame(id = url_n, wordform = NA_character_, url = urls[url_n]))
}
  })
  beep()
}

data.frame(results) %>% 
  write.csv("polish_dictionary_1.csv")

