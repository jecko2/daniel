from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import View
from django.views import generic
from article.models import Post
from tags.models import Tag
from django.db.models import Q
import random
import datetime
from contacts.forms import PostCommentForm
from contacts.models import Comment
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class LandingHomeView(View):
    template_name = "index.html"
    model = Post

    def get(self, *args, **kwargs):
        
        

        
        context = {}
        try:
            context.update({
                
                
                # Filter for Header
                
                "technology":random.sample(list(self.model.objects.filter(tag__name="Technology").all()),k=6),
                "lifestyle":random.sample(list(self.model.objects.filter(tag__name="lifestyle").all()), k=6),
                "education":random.sample(list(self.model.objects.filter(tag__name="Education").all()), k=6),
                "politics":random.sample(list(self.model.objects.filter(tag__name="Politics").all()), k=6),
                "sports":random.sample(list(self.model.objects.filter(tag__name="sports").all()), k=6),
                "health":random.sample(list(self.model.objects.filter(tag__name="Health").all()), k=6),

                "posthero1": random.sample(list(self.model.objects.all()), k=1)[0],
                "posthero2": random.sample(list(self.model.objects.all()), k=1)[0],
                "posthero3": random.sample(list(self.model.objects.all()), k=1)[0],
                "posthero4": random.sample(list(self.model.objects.all()), k=1)[0],

                "top_posts": self.model.objects.filter(category="TOP").all().order_by("-id"),

                # -----------------
                # ================= POPULAR ===================
                "popularSideBar": random.sample(list(self.model.objects.filter(category__iexact="POPULAR").all()), k=4),
                "popularLife": random.sample(
                    list(self.model.objects.filter(
                        Q(category__iexact="POPULAR") & Q(tag__name__iexact="lifestyle")).all()),
                    k=4),

                # ---------------------
                # =================== POPULAR PER TAGS ===============

                "popularLifestyle": random.sample(
                    list(self.model.objects.filter(Q(tag__name__iexact="lifestyle") & Q(category__iexact="POPULAR")
                                                   ).all()), k=1)[0],
                "popularSports": random.sample(
                    list(
                        self.model.objects.filter(category__iexact="POPULAR").filter(tag__name__iexact="sports").all()),
                    k=4),
                "popularSport": random.sample(
                    list(self.model.objects.filter(Q(tag__name__iexact="sports") & Q(category__iexact="POPULAR")
                                                   ).all()), k=1)[0],
                "popularpolitics": random.sample(
                    list(self.model.objects.filter(
                        Q(tag__name__iexact="politics") & Q(category__iexact="POPULAR")).all()), k=4),
                "popularpolitic": random.sample(
                    list(self.model.objects.filter(Q(tag__name__iexact="politics") & Q(category__iexact="POPULAR")
                                                   ).all()), k=1)[0],

                "populartechnologies": random.sample(
                    list(self.model.objects.filter(
                        Q(tag__name__iexact="technology") & Q(category__iexact="POPULAR")).all()), k=4),
                "populartechnology": random.sample(
                    list(self.model.objects.filter(Q(tag__name__iexact="technology") & Q(category__iexact="POPULAR")
                                                   ).all()), k=1)[0],

                # ---------------------
                # =================== CATEGOFRY ====================

                "category": random.sample(list(Tag.objects.all()), k=4),

                # ------------------------
                # ===================== TAGS ==================
                "tags": Tag.objects.all(),
                "latestSide": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=4),
                "latest": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=3),
                "latest1": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=1)[0],
                "latestFooter": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=2),

                # ------------------------
                # =================== Most Viewed : Popular

                "mostPopular": random.sample(
                    list(self.model.objects.filter(category__iexact="POPULAR").all()), k=4
                ),
                
                "mustRead": random.sample(
                    list(self.model.objects.filter(category__iexact="MEDICAL").all()), 
                    k=4
                ),
                "reminder": random.sample(list(
                    self.model.objects.all().order_by("-id")
                    ), k=4),
                
                "trending": random.sample(list(self.model.objects.filter(category="TOP").all()), k=4)

            })

        except:
            context.update({"detail": "Some data not found"})
        return render(self.request, self.template_name, context)


landing_home_view = LandingHomeView.as_view()


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    post_comment_form = PostCommentForm
    
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pub_date__year=kwargs.pop("year"), pub_date__month=kwargs.pop("month"), pub_date__day=kwargs.pop("day"), slug=kwargs.pop("slug"))
        context={
            self.context_object_name: post,
            "latest": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=3),
            "trending": random.sample(list(self.model.objects.filter(category="TOP").all()), k=3),
             "popular": random.sample(
                    list(self.model.objects.filter(category__iexact="POPULAR").all()), k=3
                ),
             "tags": Tag.objects.all(),
             "latestFooter": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=2),
             "commentform":self.post_comment_form(),
             "comments":Comment.objects.filter(post=post, is_valid=True).all()
            }
        return render(request, self.template_name, context)
    
    
    def post(self, *args, **kwargs):
        post = get_object_or_404(Post, pub_date__year=kwargs.pop("year"), pub_date__month=kwargs.pop("month"), pub_date__day=kwargs.pop("day"), slug=kwargs.pop("slug"))

        # if "post_comment" in self.request.POST:

        form = self.request.POST
        print(form)
        messages.success(self.request, "You comment was posted succesfully. and is Under review by our bots. It will be posted in a short while.")
        # return JsonResponse("success")
            # return redirect(post)
        messages.error(self.request, "Sorry, your comment was not posted. Kindly try again.")
        return redirect(post)
        # return 
        
    
    
    
post_detail_view = PostDetailView.as_view()




class PostListPerTagView(View):
    model = Post
    template_name = "tag_list.html"
    
    def get(self, request, *args, **kwargs):
        post = get_list_or_404(Post, tag__name=kwargs.pop("tag"))
        context = {
            "posts": post,
            "tags": Tag.objects.all(),
            "latestFooter": random.sample(list(self.model.objects.filter(pub_date__hour__lte=10).all()), k=2),
            }
        return render(request, self.template_name, context)
    
    
post_list_per_tag_view = PostListPerTagView.as_view()



    