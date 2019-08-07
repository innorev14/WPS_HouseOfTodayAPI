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
    - fix: serializers class name - Exclude the name 'List'
    - fix: Product models - Products/detail_mfc charField max length 50 -> 200 and migrate
    - fix: Product models - Products/Product_thumnail, Product_detail_images \_\_str\_\_ return value
    - fix: Product models - Add ImageField path
    
- 19.07.16
    - fix: Product models - Products/detail_cost, detail_standard // CharField -> TextField
    - feat: pip install django-cors-headers and update settings.py
    - fix: Product models - ImageField -> TextField
    - fix: Product models - Products/detail_component, detail_auth // CharField -> TextField Change.
    - feat: product_crawling.py and add gitignore
    - feat: pip install bs4
    - feat: pip install ipython and add Product_crawling.ipynb

- 19.07.17
    - feat: Add the Payments app
    - feat: Add the Serializers API - category, product, product_thumnail, product_detail_image with 'list' and '\<int:pk\>'
    - fix: Products model all renewal - name, field
    - feat: Add the Serializers API - product_option with 'list' and '\<int:pk\>'
    - fix: Products image model \_\_str\_\_ return value
    
- 19.07.18
    - fix: Products model - Review // TextField -> ImageField
    - feat: Add the Products model - Review - 'star_score' DecimalField
    - fix: Change the Products model - Review - 'star_score' DecimalField -> FloatField
    - fix: Change the API serializers.py - devide the \[ProductDetailSerializer, ProductSerializer\], \[CategorySerializer, CategoryDetailSerializer\] and remove url path the \[thumnail/list/ and \<int:pk\>, detail_image/list/ and \<int:pk\>, option/list/ and \<int:pk\> \]
    - fix: Update ReviewAdmin field and add ReviewAdmin
   
- 19.07.19
    - feat: Add(Change) the API serializers.py - PDQnASerializer, ReviewSerializer
    - feat: Add(Change) the API serializers.py - ProductSerializer // Add the filtering 'thumnail_images' Attribute: Many -> Just One
    - feat: pip install drf_yasg and add API document description
    - feat: Add(Change) the API serializers.py - ProductSerializer // Add the 'review' field
    - test: git merge test
    
- 19.07.22    
    - feat: Add the StoreHome API(combine the multiple serializer in views.py) in api_views.py-StoreHomeView
    - fix: Add the admin.py-ProductAdmin-'discount_rate' field, settings.py-'rest_framework_swagger' annotate use.
    - feat: Add the RankingView API(combine the multiple serializer in views.py) in api_views.py-RankingView
    - feat: Add RankingView and StoreHoneView API description
    
- 19.07.23
    - fix: Update requirements.txt // django-extensions==2.2.1
    - feat: Add the API serializers.py(ReviewCreateSerializer, ReviewUpdateSerializer, PDQnACreateSerializer), api_views.py(ReviewCreateAPIView, ReviewUpdateAPIView, PDQnACreateAPIView, PDQnADeleteAPIView), in connect urls 4 counts.
    - feat: Add the calculate_review signal class and Update API description
    - fix: delete ProductSerializer class // review
    - feat: Update requirements.txt, cron.py // django-crontab==0.7.1
    - feat: Create the models.py - class // HotDealNumber
    - fix: Update StoreHomeView // add updated_hot_deal_num function and update get_queryset_product function
    - fix: Update urls: StoreHomeView, ranking // StoreHomeView : Sorting all fields('categories','popular_products') except 'todaydeal', Sorting all fields(8 fields)

- 19.07.24
    - fix: setting.py - TIME_ZONE : 'UTC' -> 'Asia/Seoul'
    - feat: Create the models.py-ProductOrderCart // serializers.py-ProductOrderCartCreateSerializer, ProductOrderCartSerializer // api_views.py-ProductOrderCartAPIView, ProductOrderCartCreateAPIView // urls.py-cart/, cart/list/ // admin.py-HotDealNumberAdmin, ProductOrderCartAdmin // mean : create shopping basket.
    - fix: Accounts model - User // type, unique_user_id and AddSocialLoginBackend class
    - feat: Accounts model makemigrations and migrate
    - fix: settings.py - AUTHENTICATION_BACKEND // 'accounts.backends.SocialBackend' -> 'accounts.backends.SocialLoginBackend'
    - fix: Add the models.py-ProductOrderCart Fields //'recipient','rec_zipcode','rec_address1','rec_address2','rec_phone_number','rec_comment','orderer_name','orderer_email','orderer_phone_number','total_product_price','deliver_price','total_payment'

- 19.07.25
    - fix: Update Accounts model and backends.py - SocialLoginBackend

- 19.07.26
    - feat: Create the models.py-ProductOrderCart, Payment, OrderProduct // admin.py-ProductOrderCartAdmin, PaymentAdmin, OrderProductAdmin // serializers.py-ProductOrderCartSerializer, PaymentCreateSerializer // api_views.py-ProductOrderCartCreateAPIView, ProductOrderCartAPIView, PaymentCreateAPIView + receiver to after_payment // urls.py-'cart/', 'cart/list/', 'payment/' // Add the after_payment signal class and Update API description (auto calculated)
    - fix: Products models // Payment - field delete
    - fix: Products serializer and api_view // Payment, OrderProduct
    
- 19.07.30
    - fix: Add the API serializers.py-ProductOrderCartSerializer // Add the ProductThumnail image One. -> field name : 'image'
    - feat: Create the models.py-DirectPayment // It was added for direct payment.
    - feat: Make Project app - community
    - feat: Create the API serializers.py-DirectPaymentCreateSerializer // api_views.py-DirectPaymentCreateAPIView, @receiver-after_direct_payment // urls.py-url('payment/direct/') // admin.py-DirectPaymentAdmin // Main content: When a record is added to 'DirectPayment', the record is automatically saved to 'OrderProduct'.
    - fix: products-api_views.py-ProductOrderCartAPIView : add the swagger comment 'image' // accounts-admin.py-CustomUserAdmin : add the 'social_profile' in list_display
    - fix: re import the products-api_views.py-PaymentCreateAPIView // re import

- 19.07.31
    - fix: accounts - serializers.py // Add UserSerializer 'type', 'social_profile' field
    - feat: add the models.py-CronLog // admin.py-CronLogAdmin // remove the api_views.py-StoreHomeView HotDealNumber (comment: Create random int code.) --> Add the cron.py-my_scheduled_job (comment: Create random int code.) // The number of 'HotDealNumber' models was set to automatically change to crontab at midnight every day.
    - feat: Add community model // Housewarming, DetailContent, HousewarmingComment
    - fix: Add the community-models.py-DetailContent Connect ForeignKey // fix the settings.py-CRONJOBS
    - fix: Update products model // OrderItem, Order


- 19.08.01
    - fix: add the coummnity app makemigrations & migrate -> models.py-(Double the maximum_length text volume of the model.) & change settings.py-CRONJOBS (* 0 * * *) -> (0 0 * * *) (Changed the execution time of CRONJOBS)
    - fix: Update products // OrderItem and Order serializers, api_views

- 19.08.02
    - fix: Update products // OrderItem and Order serializers, api views - Add the brand_name
    - fix: Update products // OrderItemUpdateSerializer - Add the total_price
    - feat: Update community // serializers.py-PhotoDetailSerializer, HousewarmingSerializer, HousewarmingDetailContentSerializer, HousewarmingCommentSerializer, HousewarmingDetailSerializer, community // api_views.py-HousewarmingAPIView, HousewarmingDetailAPIView, CommunityHomeAPIView, community // urls.py-path('housewarming/, housewarming/<int:pk>/, home/' Added API to community side.(including community home) && Update community // models.py-HotStoryNumber, admin.py-HotStoryNumberAdmin + products-cron.py-my_scheduled_job --> Community Home Page is also added to the cronjobs action.
    - fix: Update accounts // delete null attribution of email field
    - fix: Update products // OrderFromCartCreateAPIView,OrderDirectCreateAPIView - Add the replace()
    - fix: Update products // OrderFromCartCreateAPIView,OrderDirectCreateAPIView - request.POST -> request.data
    - fix: change the Markdown(url - 'swagger/v1'), change the community-api_views.py-CommunityHomeAPIView-'today_picture' API data. (url - community/home/) + Create the community-serializers.py-TodayPictureSerializer class.
    - fix: test the django-crontab, added a method of use as an comment(settings.py-CRONJOBS)

- 19.08.05
    - fix: change the accounts-models.py-User-class Meta
    - feat: It separated 'crontab.py' from each app and made it work. Also, the 'cronjob_comment' field was added to CronLog Class. 1) Add the community-models.py-CronLog, admin.py-CronLogAdmin, cron.py-community_todaystory 2) Change(Update) the products-models.py-CronLog, admin.py-CronLogAdmin, cron.py-products_todaydeal.
    - fix: Update products // OrderItemResponseSerializer, OrderItemSerializer add the product_id
    - fix: Update products // OrderItem and Order class Meta ordering 'id'
    - fix: Update the products-Housewarming class- in 'budget' field.  
    - fix: Add the Comment community-api_views.py-HousewarmingDetailAPIView-'budget' field. // community-models.py-DetailContent-'text' field -> add the (blank=Ture)
    - fix: Change(Add) the community // serializers.py-PhotoSerializer-'author_profile_image' field. and api_views.py add the comment PhotoListAPIView class.

- 19.08.06
    - fix: Update community // PhotoListAPIView add the product_image, product_id field
    - fix: Update products // OrderItemResponseSerializer, OrderItemSerializer to_representation()

- 19.08.07
    - fix: Update community // PhotoSerializer add the author_profile_comment field
    - fix: Update accounts // Add custom permissions to UserUpdateView, UserDetailView, UserDeleteView
    - fix: Update community // Housewarming model - Change name(author_profile -> author_profile_image)
    - feat: Update community // Housewarming model - Add the author_profile_comment