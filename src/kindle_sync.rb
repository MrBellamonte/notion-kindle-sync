#!/usr/bin/env ruby
require 'date'
require 'yaml'
require 'json'
require 'kindle_highlights'

config = YAML.load_file('/Users/simons/Programming/notion-kindle-sync/config.yaml')


kindle = KindleHighlights::Client.new(
	email_address: config['kindle_cred']['email'],
	password: config['kindle_cred']['password']
)

highlights = Hash.new
books = Hash.new
for book in kindle.books do
    books[book.asin] = book.title
    highlights.merge({book.asin => []})
    highlights_temp = []   
	for highlight in kindle.highlights_for(book.asin) do
		dict_temp = { "book_id" => book.asin, "book_title"  => book.title,"author"=> book.author, "text" => highlight.text, "location" => highlight.location }
		highlights_temp << dict_temp
        
	end
    
    highlights[book.asin] = highlights_temp
end

File.open("/Users/simons/Programming/notion-kindle-sync/data/kindle_highlights.json","w") do |f|
	f.write(highlights.to_json)
 end

 File.open("/Users/simons/Programming/notion-kindle-sync/data/kindle_books.json","w") do |f|
	f.write(books.to_json)
 end



 