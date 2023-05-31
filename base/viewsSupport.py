from . models import WorkImage
from django.core.paginator import Paginator

# This function takes 3 parameters as arguments
# ...model_name: name of model from which the query or queryset 
# ... ...is to be returned from.
# ...queryset_size: when specified, this function returns the 
# ... ...queryset from index 0 to queryset_size-1 from the model.
# ... ...it defaults to None and if not specified, returns 
# ... ...whole queryset from the model if keyword is also None
# ... ...or a single query if keyword is specified. 
# ...keyword: when specified, returns a single query whose name 
# ... ...matches with the keyword.
# queryset_size & keyword should not be used together.
def get_image_or_client(model_name, queryset_size=None, keyword=None):

    if keyword == None:
        query = model_name.objects.all()[:queryset_size]
    else:
        query = model_name.objects.get(name__iexact = keyword)

    return query

# This function takes pk as argument and returns a single query
# ...whose id mathes with the pk.  
def get_work_image(pk = None):

    # To handle pk values 0, negative and that doesn't exist. 
    last_image_id = WorkImage.objects.all().last().id 
    pk = 1 if pk <= 1 or pk > last_image_id else pk
    work_image = WorkImage.objects.get(id=pk)

    return work_image

# Total n page nos. are divided into m sets of page nos. of 
# size "page_no_set" (currently 3).
# This function takes current page (active one) & the size of 
# ...page nos. set that is displayed (currently, pageNo_set = 3) 
# ...on a sinlgle page. And returns an index from m i.e. 
# ...index of the set (of size, page_no_set = 3) which the 
# ...current page falls in.  
def get_pageNo_set_index(current_page, page_no_set):

    if current_page%page_no_set == 0:
        page_no_set_index = (current_page//page_no_set)-1
    else:
        page_no_set_index = current_page//page_no_set

    return page_no_set_index

# Returns the set of page nos. that is to be displayed on the
# ...current page. 
# ... ...e.g. [1,2,3] or [4,5,6], and so on if pageNo_set = 3.
def get_pageNo_display_list():
    
    pageNo_set = 3
    total_pages = paginator_image.page_range
    current_page = work_images_perPage.number

    if current_page < 1:
        pageNo_set_index = 0
    elif current_page > 0 and current_page < len(total_pages):
        pageNo_set_index = get_pageNo_set_index(current_page, pageNo_set)
    else:
        pageNo_set_index = get_pageNo_set_index(len(total_pages), pageNo_set)
        
    start = pageNo_set_index*pageNo_set
    pageNo_display_list = total_pages[start:start+pageNo_set]

    return pageNo_display_list

# Main function of pagination on Projects page that returns the
# queryset of work images that is to be displayed on one page. 
def get_work_images_perPage(request):
    global paginator_image, work_images_perPage
    work_images_count_perPage = 1

    work_images = WorkImage.objects.all()
    paginator_image = Paginator(work_images, work_images_count_perPage)
    page_number = request.GET.get('page')

    work_images_perPage = paginator_image.get_page(page_number)

    return work_images_perPage
