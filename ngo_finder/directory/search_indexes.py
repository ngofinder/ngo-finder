from haystack.indexes import *
from haystack import site
from models import Organization

class OrganizationIndex(SearchIndex):
	text = CharField(document=True, use_template=True)
	sector = CharField(model_attr='sector')

site.register(Organization, OrganizationIndex)	
