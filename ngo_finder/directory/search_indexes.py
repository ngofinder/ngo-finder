from haystack.indexes import *
from haystack import site
from models import Organization, Comment

class OrganizationIndex(SearchIndex):
	text = CharField(document=True, use_template=True)

class CommentIndex(SearchIndex):
	text = CharField(document=True, use_template=True)

site.register(Organization, OrganizationIndex)	
site.register(Comment, CommentIndex)
