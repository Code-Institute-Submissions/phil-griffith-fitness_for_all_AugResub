[< Back to README.md](../README.md)

# Testing #

The following tests have been completed during the development of this site.

### Navigation Bar ###
---



#### Nav Bar links (Not signed in ) ####
* Click Home
  * Expect: Home page to load
* Click Shop
  * Expect: Shop page to load
* Click Members Area
  * Expect: dropdown menu showing:
    * Sign In
    * Join  
  * Click Sign In
    * Expect: Sign in page to load
  * Click Join 
    * Expect: Sign up page to load

#### Nav Bar links (Signed in - Free Member ) ####
* Click Home
  * Expect: Home page to load
* Click Shop
  * Expect: Shop page to load
* Click Members Area
  * Expect: dropdown menu showing:
    * My Profile
    * Sign Out  
  * Click My Profile
    * Expect: My Profile page to load
  * Click Sign Out
    * Expect: Sign Out page to load asking for confirmation
      * Click Sign Out
        * Expect: Home page to load with toast message 'sign out success'



#### Nav Bar links (Signed in as Full Member) ####
* Click Home
  * Expect: Home page to load
* Click Shop
  * Expect: Shop page to load
* Click Members Area
  * Expect: dropdown menu showing:
    * Workouts
    * Member Profiles
    * Member Blog
    * My Profile
    * Sign Out
  * Click Workouts
    * Expect: Workouts page to load
  * Click Member Profiles
    * Expect: Member Profiles page to load
  * Click Member Blog
    * Expect: Member Blog page to load
  * Click My Profile
    * Expect: My Profile page to load
  * Click Sign Out
    * Expect: Sign Out page to load asking for confirmation
      * Click Sign Out
        * Expect: Home page to load with toast message 'sign out success'

#### Nav Bar links (Signed in as Admin) ####
* Click Home
  * Expect: Home page to load
* Click Shop
  * Expect: Shop page to load with Edit & Delete buttons for each product and an Add Product button
* Click Members Area
  * Expect: dropdown menu showing:
    * Workouts
    * Member Profiles
    * Member Blog
    * My Profile
    * Sign Out
  * Click Workouts
    * Expect: Workouts page to load with Edit & Delete buttons for each workout and an Add Workout button
* Click Member Profiles
  * Expect: Member Profiles page to load
* Click Member Blog
  * Expect: Member Blog page to load
* Click My Profile
  * Expect: My Profile page to load
* Click Sign Out
  * Expect: Sign Out page to load asking for confirmation
    * Click Sign Out
      * Expect: Home page to load with toast message 'sign out success'



### Shop ###
---

#### Search ####

* Enter search term in search bar and click Search or press Enter
  * Expect: Any matching products to be displayed
* Click Reset
  * Expect: Search term to be cleared and Shop to reload showing all results
* Click on a Product
  * Expect: Product detail page to load
* Click Category filter dropdown and chose Equipment
  * Expect: Products with equipment category to be shown
* Click Category filter dropdown and chose Clothing
  * Expect: Products with clothing category to be shown
* Click Category filter dropdown and chose Accessories
  * Expect: Products with accessories category to be shown
* Click Category filter dropdown and chose Nutrition
  * Expect: Products with nutrition category to be shown
* Click Sort by and chose Price (Low to high)
  * Expect: Products to be sorted by price (lowest first)
* Click Sort by and chose Price (high to low)
  * Expect: Products to be sorted by price (highest first)
* Click Sort by and chose Name (A-Z)
  * Expect: Products to be sorted by Name (A-Z)
* Click Sort by and chose Name (Z-A)
  * Expect: Products to be sorted by Name (Z-A)

#### Product Detail page ####

* Click up/down arrows in qunatity field
  * Expect quantity to change
* Click Add to Basket
  * Expect item to be added to basket, basket icon to show update total for basket and toast success message to confirm item added
* Click Remove
  * Expect item/s to be removed and toast meesage to confirm
* Click Checkout
  * Expect checkout page to load


&nbsp;
### Checkout ###
---

* Complete all form fields and add invalid card details then click Complete Order
  * Expect: Error message - Your card number is invalid
* Complete all form fields and add valid card details then click Complete Order
  * Expect: Spinning processing icon and then a confirmation page advising that an email has been sent. Email should be received.


#### Full Member ####
  * Expect: Member discount to be showing and total to be discounted by 10%
  * Complete all fields of address and click the Save delivery information to my profile, then complete checkout
  * Expect: Address details to be added to users profile and order to be showing in user profile order history



&nbsp;
### Workouts ###
---

##### Full member or Admin (Signed in) #####
* Click workout category dropdown and select Stength
  * Expect: All workouts in Strength category to be shown
* Click workout category dropdown and select Cardio
  * Expect: All workouts in Cardio category to be shown
* Click workout category dropdown and select Toning
  * Expect: All workouts in Toning category to be shown
* Click workout category dropdown and select HIIT
  * Expect: All workouts in HIIT category to be shown
* Click RESET
  * Expect: Category filter to change to All workouts and all workouts to be shown
* Click any workout
  * Expect: Workout video to be displayed with a desctipion
##### Admin only (Signed in) #####
* On Add Product 
  * Expect: Add Product Form page to load
* On Edit on any product 
  * Expect: Edit Product Form page to load
* On Delete on any product 
  * Expect: Modal requesting confirmation to load
    * Click Cancel
      * Expect: Modal to close and product to remain
    * Click Yes
      * Expect Modal to close and product to be removed

&nbsp;
### Member Profiles ###
---

##### Full member or Admin (Signed in) #####

* Expect: All full member profiles to be displayed, showing the following details if added by member:
  * Profile Picture
  * Username
  * Name
  * Age
  * Fitness Goal

&nbsp;
### Member Blog ###
---

##### Full member or Admin (Signed in) #####

* Expect: All blogs from members to be displayed, with abilty to scroll
* Click Add Blog
  * Expect: Add blog page to load with an input for title and comment / blog
    * Click Cancel
      * Expect: Member Blog page to load
    * Click Submit
      * Expect: Blog to be added to member blogs

&nbsp;
### My Profile ###
---
##### Free Member, Full member or Admin (Signed in) #####

* Expect: Page to load displaying Public profile and the following additional page tabs:
  * Full Profile
    ##### Free Member (Signed in) #####
    * Expect: Membership status to show Free and an upgrade button to be visible
    ##### Free Member (Expired Full Memebership) (Signed in) #####
    * Expect: Membership status to show Free and a Renew button to be visible
    ##### Full member or Admin (Signed in) (Signed in) #####
    * Expect: Membership status to show Full with no button for Renew / upgrade and Membership Expiriry date should be later than today or never (Admin)
    ##### Free Member, Full member or Admin (Signed in) #####
    * Click Edit Profile
      * Expect: Edit profile form page to load
  * Order History


&nbsp;
### Form Validations ###
---

#### Signup Form ####

* Enter invalid email address (without @) and click Submit
  * Expect: Validation popup request '@' symbol

* Enter non matching email (again) and click SUbmit
  * Expect: Validation message stating email must match

* Complate form without username and click Submit
  * Expect: Validation popup requesting for field to be completed
* Complate form without First Name and click Submit
  * Expect: Validation popup requesting for field to be completed
* Complate form without Last Name and click Submit
  * Expect: Validation popup requesting for field to be completed
* Complate form without Password and click Submit
  * Expect: Validation popup requesting for field to be completed
* Complate form without Password (again) and click Submit
  * Expect: Validation popup requesting for field to be completed
* Complate form without Password (again) and click Submit
  * Expect: Validation popup requesting for field to be completed
* Enter different password (again) and click Submit
  * Expect: Validation message stating same password must be typed
* Select Free membership and click Submit
  * Expect new user to be created with Full Member expiry of today
* Select Full 30 days and click Submit
  * Expect new user to be created with Full Member expiry of 30 days after today
* Select Full 6 months and click Submit
  * Expect new user to be created with Full Member expiry of 180 days after today
* Select Full 1 year and click Submit
  * Expect new user to be created with Full Member expiry of 365 days after today

#### Sign In Form ####

* Enter incorrect username for known account and correct password then click Sign In
  * Expect: Message stating username and or password is incorrect
* Enter correct username for known account and incorrect password then click Sign In
  * Expect: Message stating username and or password is incorrect

#### Edit profile Form ####

* All fields are optional so no validations are expected
* Click Update profile
  * Expect: toast success message to popup and to be returned to the Profile page
* Click Choose File  (for Profile image)
  * Expect Local file explorer window to open for file selection. Select file and click open / confirm, then click Submit
    * Expect: Toast success message, Profile page to load and image to be displayed on profile
* Click clear next to image file name (If added) and click Submit
  * Expect image to be removed from profile


#### Edit Product Form (Admin only) ####

* Complete Form without Name and click Submit
  * Expect: Validation popup prompting to complete field
* Complete Form without Price and click Submit
  * Expect: Validation popup prompting to complete field
* Click Choose File  (for product image)
  * Expect Local file explorer window to open for file selection. Select file and click open / confirm, then click Submit
    * Expect: Toast success message, Product page to load and image to be displayed
* Click clear next to image file name (If added) and click Submit
  * Expect image to be removed from product

#### Edit Workout Form (Admin only) ####

* Complete Form without Name and click Submit
  * Expect: Validation popup prompting to complete field
* Complete Form without video url and click Submit
  * Expect: Validation popup prompting to complete field
* Click Choose File  (for workout image)
  * Expect Local file explorer window to open for file selection. Select file and click open / confirm, then click Submit
    * Expect: Toast success message, Workout page to load and image to be displayed
* Click clear next to image file name (If added) and click Submit
  * Expect image to be removed from workout


&nbsp;
### Site Security ###
---

#### Non-member / guest ####

* Try to access edit product page by editing url
  * Expect: To be redirected to Sign In page
* Try to access add product page by editing url
  * Expect: To be redirected to Sign In page
* Try to access workouts page by editing url
  * Expect: To be redirected to Sign In page
* Try to access edit workout page by editing url
  * Expect: To be redirected to Sign In page
* Try to access add workout page by editing url
  * Expect: To be redirected to Sign In page
* Try to access Member Blog page by editing url
  * Expect: To be redirected to Sign In page
* Try to access Add Blog page by editing url
  * Expect: To be redirected to Sign In page
* Try to access Member Profiles page by editing url
  * Expect: To be redirected to Sign In page

#### Free member  ####
* Try to access edit product page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access add product page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access workouts page by editing url
  * Expect: To be redirected to Home page
* Try to access edit workout page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access add workout page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access Member Blog page by editing url
  * Expect: To be redirected to Home page
* Try to access Add Blog page by editing url
  * Expect: To be redirected to Home page
* Try to access Member Profiles page by editing url
  * Expect: To be redirected to Home page

#### Full member  ####

* Try to access edit product page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access add product page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access edit workout page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.
* Try to access add workout page by editing url
  * Expect: To be redirected to Home page and toast message to display, stating only store owners can do that.






### User Story Testing ###
---

#### As User ####

* <strong>Have access to exercise and nutrition products</strong>
  * Click Shop button on navbar whilst signed out - Shop page loads displaying all products


    ![](/documentation/images/shop.png)




    &nbsp;
* <strong>See what the site has to offer before becoming a full member</strong>
  * The home page details all member benfits
  

    ![](/documentation/images/member_benefits.png)

&nbsp;

#### As Member ####

* <strong>Get discounts for products</strong>
  * Full Members are given a 10% dicount

    ![](/documentation/images/member_discount.png)

* <strong>See order history</strong>
  * An Order history page is availble from the My Profile page

    ![](/documentation/images/order_history.png)

* <strong>Have access to a variety of workout videos</strong>
  * Workout videos are availble for full members

    ![](/documentation/images/workouts.png)

* <strong>Be able to view specific workouts for different fitness goals</strong>
  * Workouts can be filtered by category

    ![](/documentation/images/workout_category.png)

* <strong>Have access to exercise and nutrition advice</strong>
  * Full members are granted access to 1 to 1 coaching advice sessions

* <strong> Ability to share my progress and view other members progress </strong>
  * Full members can share updates with other members via the Member Blog

    ![](/documentation/images/member_blog.png)

&nbsp;

#### As Site Owner ####

* <strong>Sell branded exercise products </strong>
  * Branded exercise products can be sold in the Shop

    ![](/documentation/images/exercise_equipment.png)

* <strong>Sell nutritiuonal products </strong>
  * Nutritional products can be sold in the Shop

    ![](/documentation/images/nutrition.png)

* <strong>Manage products</strong>
  * Products can be edited, removed and added via the Shop or product detail page when logged in as a superuser / admin.

    ![](/documentation/images/edit_delete_prod.png)

    ![](/documentation/images/prod_manage.png)

    ![](/documentation/images/delete_product_confirm.png)

    ![](/documentation/images/add_prod_but.png)

    ![](/documentation/images/prod_manage_add.png)

* <strong>Manage Workout Videos</strong>
  * Workouts can be edited, removed and added via the Workouts page or workout detail page when logged in as a superuser / admin.

    ![](/documentation/images/edit_delete_workout.png)

    ![](/documentation/images/workout_manage.png)

    ![](/documentation/images/delete_workout_confirm.png)

    ![](/documentation/images/add_workout_but.png)

    ![](/documentation/images/workout_manage_add.png)



