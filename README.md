# habrahabr posts parser
parsed data structure:
-list of posts
	-post is the dict with fields: title, hubs and article
		-title is the string(text)
		-hubs is the list of hubs
			-hub is the dict with fields: name and link
				-name is string(text)
				-link is string(url)
			-article is the dict with fields: text, images and links
				-text is sting(text)
				-images is the list of strings(urls)
				-links is the list of links
					-link is the dict with fields: text and link
						-text is the string(text)
						-link is the string(url)
