from __future__ import print_function
import oci
import sys

config = oci.config.from_file(
    '__PATH__TO_CONFIG__FILE__',
    'DEFAULT'
)

search_client = oci.resource_search.ResourceSearchClient(config)


def search_with_free_text(string_to_search):
    free_text_search = oci.resource_search.models.FreeTextSearchDetails(text=string_to_search,
                                                                        type='FreeText',
                                                                        matching_context_type=oci.resource_search.models.SearchDetails.MATCHING_CONTEXT_TYPE_HIGHLIGHTS)
    for response in oci.pagination.list_call_get_all_results_generator(search_client.search_resources, 'response',
                                                                       free_text_search):
        for resource in response.data.items:
            print("Resource type: {}, Resource name: {}".format(resource.resource_type, resource.display_name))


ocid = str(sys.argv.pop())
search_with_free_text(ocid)


