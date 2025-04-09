from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request,'multipageApp/index.html')

def movies_info(request):
    head_msg = "Movies Information"
    sub_msg1 = "Marvel Movies is faviorate of maximum Youngstart and child"
    sub_msg2 = "It is a hollywood movies and it gives us about super power"
    sub_msg3 = "Action is best of Hollywood movies"
    type = "movies"

    my_dict = {"head_msg":head_msg, "msg1":sub_msg1, "msg2":sub_msg2, "msg3":sub_msg3, "type":type}
    return render(request, 'multipageApp/handle.html', my_dict)

def sports_info(request):
    head_msg = "Sports Information"
    sub_head1 = "Sports is a physical exercise of human life"
    sub_head2 = "Anyone can activity of one sports"
    sub_head3 = "Sports is good for health"
    type = "sports"

    my_dict = {"head_msg":head_msg, "msg1":sub_head1, "msg2":sub_head2, "msg3":sub_head3, "type":type}

    return render(request, 'multipageApp/handle.html', my_dict)

def politics_info(request):
    head_msg = "Politics Information"
    sub_head1 = "Every country has going on politics"
    sub_head2 = "India Prime minister is Narendra Damodar Modi"
    sub_head3 = "Every 5 years politics party may be change or not"
    type = "politics"

    my_dict = {"head_msg":head_msg, "msg1":sub_head1, "msg2":sub_head2, "msg3":sub_head3,
               "type":type}

    return render(request, 'multipageApp/handle.html', my_dict)