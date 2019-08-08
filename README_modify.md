# WPS_HouseOfTodayAPI

FinalProject - House of Today API

## Team members
- 천정환
- 김병욱
- 구진욱
- 허성윤

## Update messages

- 19.07.11
    - feat: Start django Project(base config)
    - feat: Connect Amazon Web Services - S3, RDS
    - feat: Make Project app - accounts, products
    - feat: Make accounts models
    - feat: Make accounts serializers, views
    - feat: Make User email - admission
    - feat: Make Token
    
- 19.07.12
    - feat: Make Products models
    - feat: Make Products serializers, views - About Category
    
- 19.07.15
    - fix: products-serializers class name - Exclude the name 'List'
    - fix: products-models-Product-'detail_mfc' // change the Field Option: CharField max length 50 -> 200 and A Migrate was executed.
    - fix: products-models-Product-'Product_thumnail', 'Product_detail_images' // change the __str__ return value, int -> str  
    - fix: products-models-Product-'image' // Add ImageField path
    
- 19.07.16
    - fix: products-models-Product-'detail_cost', 'detail_standard' // change the Field Option: CharField -> TextField
    - feat: pip install django-cors-headers and update settings
    - fix: products-models-Product-'ImageFields' // The fields corresponding to 'ImageField' were changed to 'TextField's.
    - fix: products-models-Product-'detail_component', 'detail_auth' // change the Field Option: CharField -> TextField.
    - feat: Create product_crawling.py and Add the .gitignore // The file automatically saved the crawling of the product to the Postgresql DB.
    - feat: pip install bs4
    - feat: pip install ipython and add Product_crawling.ipynb

- 19.07.17
    - feat: Create the 'Payments' app - Added to execute actual payment API.(Local implementation only)
    - feat: products-serializers-ProductDetailSerializer-'thumnail_images', 'detail_images' // Added subserializer field.
    - feat: products-urls-'product/list/<int:pk>/' // Add the path ProductListView_as_view() 
    - fix: products-models-All Class, Field // renewed all the classes and fields.
    - feat: products-serializers-ProductOption // Added subserializer field.
    - feat: products-urls-'product/list/' // Add the path ProductDetailView_as_view()
    - fix: products-models-Product-'image' // change the __str__ return value, int -> str
    
- 19.07.18
    - fix: products-models-Review-'product' // change the Field Option: TextField -> ImageField
    - feat: products-models-Review-'star_score' // Add the DecimalField
    - fix: products-models-Review-'star_score' // change the Field Option: DecimalField -> FloatField
    - fix: products-serializers-['ProductDetailSerializer','ProductSerializer'], [CategorySerializer, CategoryDetailSerializer] // Make and Devide the Class.
    - fix: products-urls-['thumnail/list/', 'thumnail/<int:pk>'], ['detail_image/list','detail_image/<int:pk>'], ['option/list','option/<int:pk>'] // Add the url paths.
    - fix: products-admin-'ReviewAdmin' // Add the field.
     
- 19.07.22    
    - feat: products-api_views-StoreHomeView // Add the StoreHome API(combine the multiple serializer in views) 
    - fix: products-admin-ProductAdmin-'discount_rate' // Add the Field.
    - fix: config-settings-INSTALLED_APPS-'rest_framework_swagger' // It was annotate.
    - feat: products-api_views-RankingView // Add the API(combine the multiple serializer in views)
    - feat: products-api_views-RankingView, StoreHomeView // Add the API description.
    
- 19.07.23
    - fix: Update requirements.txt // django-extensions==2.2.1
    - feat: products-serializers-(ReviewCreateSerializer, ReviewUpdateSerializer, PDQnACreateSerializer) // Add the API serializers.
    - feat: products-api_views-(ReviewCreateAPIView, ReviewUpdateAPIView, PDQnACreateAPIView, PDQnADeleteAPIView) // Add the API Views, and descriptions.  
    - feat: products-urls-('product/review/', 'product/review/<int:pk>/', 'product/qna/', 'product/qna/delete/<int:pk>/') // in connect urls 4 counts.
    - feat: products-api_views-'calculate_review' // Add the 'calculate_review' signal class.
    - fix: products-serializers-'review' // delete 'review' field. 
    - feat: products-cron // django-crontab==0.7.1, Update requirements.txt.
    - feat: products-models-HotDealNumber // Create the model.
    - fix: products-api_views-StoreHomeView-'updated_hot_deal_num', 'get_queryset_product' // add 'updated_hot_deal_num' and 'get_queryset_product' function.
    - fix: products-api_views-StoreHomeView-('categories','popular_products') // Sorting all API fields except 'todaydeal', Sorting all fields(8 fields).
    - feat: products-urls-('storehome/','ranking/') // in connect urls 2 counts.  

- 19.07.24
    - fix: config-settings-TIME_ZONE // change the 'UTC' -> 'Asia/Seoul'
    - feat: products-models-ProductOrderCart // Create the model, It is aimed at create shopping basket.
    - feat: products-admin-('HotDealNumberAdmin', 'ProductOrderCartAdmin') // Create the Admin class. 
    - feat: products-serializers-(ProductOrderCartCreateSerializer, ProductOrderCartSerializer) // Create the serializers.
    - feat: products-api_views-(ProductOrderCartAPIView, ProductOrderCartCreateAPIView) // Create the View.    
    - feat: products-urls-('cart/', 'cart/list/') // in connect urls 2 counts.  
    - fix: accounts-models-User-('type', 'unique_user_id') // Add class for SocialLoginBackend.
    - feat: accounts-models // ./manage.py makemigrations && migrate.
    - fix: config-settings-AUTHENTICATION_BACKENDS // change the content 'accounts.backends.SocialBackend' -> 'accounts.backends.SocialLoginBackend'.
    - fix: products-models-ProductOrderCart-('recipient','rec_zipcode','rec_address1','rec_address2','rec_phone_number','rec_comment','orderer_name','orderer_email','orderer_phone_number','total_product_price','deliver_price','total_payment') // Add the Fields.

- 19.07.25
    - fix: accounts-models-User // Add model and backend for settings-SocialLoginBackend.

- 19.07.26
    - feat: products-models-(ProductOrderCart, Payment, OrderProduct) // Create the models.
    - feat: products-admin-(ProductOrderCartAdmin, PaymentAdmin, OrderProductAdmin) // Create the admin classes.
    - feat: products-serializers-(ProductOrderCartSerializer, PaymentCreateSerializer) // Create the serializers.
    - feat: products-api_views-(ProductOrderCartCreateAPIView, ProductOrderCartAPIView, PaymentCreateAPIView, after_payment) // create the views, receiver def 'after_payment'.
    - feat: products-urls-('cart/', 'cart/list/', 'payment/') // It is Add the 'after_payment' signal class and Update API description (auto calculated)
    - fix: products-models-Payment // delete the fields in 'Payment'.
    - fix: products-api_views-(OrderProductCreateAPIView, OrderProductAPIView, PaymentCreateAPIView) // change the views.
    - fix: products-serializers-(PaymentSerializer, OrderProductSerializer) // change the serializers. 
    
- 19.07.30
    - fix: products-serializers-ProductOrderCartSerializer // Add the Serializers.
    - fix: products-serializers-ProductThumnail-'image' One. -> field name : 'image'.
    - feat: products-models-DirectPayment // Create the model, It was added for direct payment.
    - feat: Make Project app - community
    - feat: products-admin-DirectPaymentAdmin // Create the Admin class.
    - feat: products-serializers-DirectPaymentCreateSerializer // Create the serializers.
    - feat: products-api_views-(DirectPaymentCreateAPIView, @receiver-after_direct_payment) // Create the api_views and receiver def, Main content: When a record is added to 'DirectPayment', the record is automatically saved to 'OrderProduct'.
    - feat: products-urls-('payment/direct/') // in connect urls 1 counts. 
    - fix: products-api_views-ProductOrderCartAPIView-'image'(comment) // add the swagger comment 'image'.
    - fix: accounts-admin-CustomUserAdmin-'social_profile' : add the 'social_profile' in list_display.
    - fix: products-api_views-PaymentCreateAPIView // re import was carried out.

- 19.07.31
    - fix: accounts-serializers-('type', 'social_profile') // Add UserSerializer field.
    - feat: products-models-CronLog // Create the model.
    - feat: products-admin-CronLogAdmin // Create the admin class.
    - fix: products-api_views-StoreHomeView-'HotDealNumber' // remove the define 'HotDealNumber'. (comment: Create random int code.)
    - fix: products-cron-my_scheduled_job // Add the define 'my_scheduled_job'. (comment: Create random int code. The number of 'HotDealNumber' models was set to automatically change to crontab at midnight every day.)
    - feat: community-(Housewarming, DetailContent, HousewarmingComment) // Add 'community' app and 3 models. 
    - fix: community-models-DetailContent // Add the Connect ForeignKey.
    - fix: settings-CRONJOBS // change the code.
    - feat: products-models-OrderItem, Order // create the 2 models. 

- 19.08.01
    - fix: community-models // Double the maximum_length text volume of the models.
    - fix: settings-CRONJOBS // (* 0 * * *) -> (0 0 * * *) (comment: Changed the execution time of CRONJOBS)
    - fix: coummnity // ./manage.py makemigrations && migrate 
    - fix: products-serializers // change the OrderItemSerializer and OrderSerailizer.
    - fix: products-api_views // change the OrderItemAPIView and OrderAPIView.

- 19.08.02
    - fix: products-serializers(OrderItemSerializer, OrderSerializer)-brand_name // add the brand_name
    - fix: products-api_views(OrderItemAPIView, OrderAPIView)-brand_name // add the brand_name
    - fix: products-serializers-OrderItemUpdateSerializer-'total_price' // Add the field.
    - feat: community-serializers-(PhotoDetailSerializer, HousewarmingSerializer, HousewarmingDetailContentSerializer, HousewarmingCommentSerializer, HousewarmingDetailSerializer) // Create the 5 serializers. 
    - feat: community-api_views-(HousewarmingAPIView, HousewarmingDetailAPIView, CommunityHomeAPIView) // Create the 3 APIViews.
    - feat: community-urls-path('housewarming/', 'housewarming/<int:pk>/', 'home/') // in connect urls 3 counts.(Added API to community side, including community home)
    - feat: community-models-HotStoryNumber // Add the model.
    - feat: community-admin-HotStoryNumberAdmin // Add the admin model.
    - feat: products-cron-my_scheduled_job // Community Home Page is also added to the cronjobs action.
    - fix: accounts-User // delete null attribution of EmailField.
    - fix: products-serializers-(OrderFromCartCreateAPIView, OrderDirectCreateAPIView) // change the request.POST -> request.data
    - fix: products-api_views-(OrderFromCartCreateAPIView, OrderDirectCreateAPIView) // Add the replace() 2 APIViews.
    - fix: products-api_views // change the Markdown(urls-'swagger/v1')
    - fix: community-api_views-CommunityHomeAPIView-'today_picture' // change the API data(url - community/home/).
    - feat: community-serializers-TodayPictureSerializer // Create the class.
    - fix: settings-CRONJOBS // test the django-crontab, added a method of use as an comment.

- 19.08.05
    - fix: accounts-models-User // change the 'class Meta'.
    - feat: 1) community-models-CronLog // Add the model.
    - feat: 2) community-admin-CronLogAdmin // Add the admin model.
    - feat: 3) community-cron-community_todaystory // Add the 'community_todaystory' define.
    - fix: 4) products-models-CronLog // Change the model.
    - fix: 5) products-admin-CronLogAdmin // Change the admin model.
    - fix: 6) products-cron-products_todaydeal // Change the 'products_todaydeal' define. [1~6)total theorem: It separated 'crontab' from each app and made it work. Also, the 'cronjob_comment' field was added to CronLog Class.]
    - fix: products-serializers-(OrderItemResponseSerializer, OrderItemSerializer)-'product_id' // Change(Add) the 'product_id' field.
    - fix: products-models-(OrderItem, Order) // Set 'ordering' of 'class meta' to 'id'.
    - fix: products-models-Housewarming-'budget' // change the 'budget' field.  
    - fix: community-api_views-HousewarmingDetailAPIView-'budget' // Add the Comment 'budget' field.
    - fix: community-models-DetailContent-'text' // Add the 'text' Field option -> (blank=Ture).
    - fix: community-serializers-PhotoSerializer-'author_profile_image' // Change(Add) the 'author_profile_image' field.
    - fix: community-api_views-PhotoListAPIView // add the comment PhotoListAPIView class.

- 19.08.06
    - fix: community-PhotoListAPIView-('product_image', 'product_id') // Change(add) the 2 fields.
    - fix: products-(OrderItemResponseSerializer, OrderItemSerializer) // Update(add) to_representation()

- 19.08.07
    - fix: community-PhotoSerializer-'author_profile_comment' // Update(add) the 'author_profile_comment' field.
    - fix: accounts-(UserUpdateView, UserDetailView, UserDeleteView) // Update(Add) custom permissions to 3 APIViews.
    - fix: community-models-Housewarming-('author_profile' -> 'author_profile_image') // Change the field name(author_profile -> author_profile_image).
    - feat: community-models-Housewarming-'author_profile_comment' // Add the 'author_profile_comment' field.
    
- 19.08.08
    - fix: products-cron-products_todaydeal // Change the 'i' 0~3 --> 1~4, 'num' 0~179 --> 1~180 change + Random random numbers were modified to prevent overlap.
    - fix: community-cron-community_todaystory // Change the 'j' 0~3, 5 --> 1~4, 5, 'num_2nd' 0~17 --> 1~18 change + Random random numbers were modified to prevent overlap.
    - fix: README.md // The contents of the 'README.md' file have been modified according to the rules.




