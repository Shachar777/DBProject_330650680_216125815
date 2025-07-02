# DBProject_330650680_216125815

**Submitters**:  
Shachar Levy – 330650680  
Yagel Kaniel – 216125815  

**System**: Streaming Service  
**Department**: Finances

---

# תוכן עניינים

1. [תיאור המערכת](#תיאור-המערכת)  
2. [מטרת המערכת](#מטרת-המערכת)  
3. [תיאור כללי](#תיאור-כללי)  
4. [מבנה הנתונים](#מבנה-הנתונים)  
5. [פונקציונליות עיקרית](#פונקציונליות-עיקרית)  
6. [תרשימים וצילומי מסך](#תרשימים-וצילומי-מסך)  
11. [שלב האינטגרציה](#שלב-האינטגרציה)
12. [מבטים](#מבטים)
13. [תכנות postgresSQL](#תכנות-postgresSQL)
14. [ממשק גרפי](#ממשק_גרפי)

---

## תיאור המערכת

המערכת עוסקת בניהול שירותי מנויים של פלטפורמת סטרימינג תוך שמירה על מידע פיננסי, כולל תשלומים, הנחות, והחזרים. היא כוללת ניהול תוכניות מנוי, תהליכי חיוב והפקת דוחות כלכליים.

---

## מטרת המערכת

המערכת נועדה לנהל את שירותי המנויים של פלטפורמת סטרימינג, תוך מעקב אחר תשלומים, החזרים, הנחות ועסקאות כספיות.

---

## תיאור כללי

- ניהול תוכניות מנוי
- שיוך מנויים לתוכניות
- חישוב תשלומים אוטומטי
- ניהול החזרים ומבצעים
- הפקת דוחות

---

## מבנה הנתונים

- **Subscription_Plans** – סוג התוכנית, תקופת המנוי, עלות חודשית  
- **Subscriptions** – מידע אישי של מנויים ותוכניתם  
- **Discounts** – גובה הנחה ותוקף  
- **Payments** – תשלומים שבוצעו  
- **Refunds** – החזרים כספיים  
- **Transactions** – סטטוס ותאריך ביצוע

---

## פונקציונליות עיקרית

- ✔️ רישום מנויים ושיוכם לתוכנית  
- ✔️ חישוב תשלומים בהתאם להנחות  
- ✔️ מעקב אחר עסקאות  
- ✔️ טיפול בהחזרים  
- ✔️ ניהול מבצעים  
- ✔️ הפקת דוחות הכנסות ותשלומים

---

## תרשימים וצילומי מסך

![image1](https://github.com/user-attachments/assets/4c3cecd1-efd8-46eb-bae7-523498f0f170)  
![image2](https://github.com/user-attachments/assets/8d1ce340-d550-4fc4-ada1-38ff7af66083)  
![image3](https://github.com/user-attachments/assets/e0bb848e-2f1a-407a-8018-e620753e0973)  
...

---

### שאילתות DELETE

1. מחיקת הנחות שפג תוקפן ולא נעשה בהן שימוש:  
   ![image](https://github.com/user-attachments/assets/2ede949b-292a-41a9-ae1a-8a438f64556b)  
2. מחיקת מנויים שלא שילמו כלל:  
   ![image](https://github.com/user-attachments/assets/ef3ce8ba-890c-470e-ae37-04c7c906d5e2)  
3. מחיקת עסקאות שכשלו לפני יותר מחצי שנה:  
   ![image](https://github.com/user-attachments/assets/6510819a-7f9b-4cf3-b1be-a9d88446a26f)

---

### שאילתות UPDATE

1. עדכון סכום תשלום לפי אחוז הנחה:  
   ![image](https://github.com/user-attachments/assets/12b664fa-e586-4f0d-a76d-d731d4a8fec9)  
2. העלאת מחירי תוכניות בישראל ב־5%:  
   ![image](https://github.com/user-attachments/assets/b62cd1f4-fad7-48de-8d10-0f3dd4509b37)  
3. שינוי סטטוס עסקאות מ-Pending ל-Failed אחרי 7 ימים:  
   ![image](https://github.com/user-attachments/assets/609bea73-b4cb-4e52-9897-ad186decc665)

---

### שאילתות SELECT

1. סכומי תשלומים חודשיים מדורגים לפי גובה הכנסות:  
   ![image](https://github.com/user-attachments/assets/bce46179-c9e4-4289-b61f-fbc0a2c71264)  
2. סוג התוכנית עם ההכנסה הגבוהה ביותר בשנה:  
   ![image](https://github.com/user-attachments/assets/f180b158-64fb-4868-9526-490deec418e6)  
3. יחס בין עלות ממוצעת לבין מספר מנויים במדינה:  
   ![image](https://github.com/user-attachments/assets/516b399b-0000-4cb8-a3ee-e3c62ec4bc3d)  
4. יחס בין הכנסה ממוצעת למספר מנויים במדינה:  
   ![image](https://github.com/user-attachments/assets/404b62c7-5358-4661-841d-8e747c3dd906)
   5. מנויים שהעסקה האחרונה שלהם נכשלה:

![image](https://github.com/user-attachments/assets/23efbec2-bd3a-4453-a9af-ed90f9d4382c)

6. המדינות בעלות כמות הרשומים הכי גדולות:
![image](https://github.com/user-attachments/assets/89339560-9fda-4807-a24a-8caeac6d7771)

7. ההחזרים הכי גבוהים:
![image](https://github.com/user-attachments/assets/5243bf6a-5267-46e8-b62d-982b5b604847)

8. השאילתה מציגה את 40 הלקוחות ששילמו הכי הרבה לאחר הנחה, כולל מספר התשלומים שביצעו:
![image](https://github.com/user-attachments/assets/e041da36-e58c-4571-8aa6-c93e1ae49497)









---

### תיאור ה-Constraints

1. כמות מכשירים – בין 1 ל־9:  
   ![image](https://github.com/user-attachments/assets/7eb9cfda-db98-4f75-a22f-975171770e5e)  
2. שם הלקוח לא יכול להיות `NULL`:  
   ![image](https://github.com/user-attachments/assets/cf9f49fd-2d5d-419e-905a-0333c95e410a)  
3. סכום התשלום – בין 0 ל־9999.99:  
   ![image](https://github.com/user-attachments/assets/2941bf62-895e-4c30-8658-a0632eb703a1)


---
## שלב האינטגרציה

## תמונות מסך של תרשימי הERD והDSD
![image](https://github.com/user-attachments/assets/2db3493d-be35-4b9b-99e3-e41abdda224c)
![Screenshot 2025-06-03 160239](https://github.com/user-attachments/assets/b83f1beb-9133-461a-a15b-a2ebbf386a6a)
![IMG-20250513-WA0025](https://github.com/user-attachments/assets/de3d0f6c-378b-46d1-92fa-1cd551eee7b0)
![IMG-20250513-WA0024](https://github.com/user-attachments/assets/25c50b5a-6f6a-44fa-a71d-29154030706e)

### תיאור ההחלטות
- צירפנו את היישויות subscriptions ו customer לישות אחת בשם customers
- צירפנו את payment ו payments לישות אחת בשם payments
- מחקנו את הישות devices משום שיש לנו כבר device_limit ב subscription_plans
- הפכנו את הישות reviews לישות חלשה מכיוון שהיא תלוייה בprofile_id, כלומר לא ייתכן שהמפתח יהיה movie_id, משום שיכול להיות כמה חוות דעת של משתמשים שונים לאותו סרט
- הפכנו את הישות favorites לישות חלשה מאותה סיבה, אותו סרט יכול להיות אהוב על ידי כמה פרופילים שונים
- שינינו שמות של עמודות כדי שיתאים לשיטת הענקת השמות שלנו

### הסבר על התהליך
שינוי שמות עמודות (Renaming Columns)
בוצעו מספר שינויים לשמות עמודות בטבלאות שונות, לדוגמה:

subscription_id שונה ל-customer_id

profilename שונה ל-profile_name

עמודות כמו isonline, profilepicture, movieid ועוד קיבלו שמות בפורמט תקני יותר, עם הפרדה באמצעות קו תחתון (snake_case), מה שמשפר קריאות ותחזוקה.

הוספת עמודות חדשות (Adding Columns)
לטבלאות נוספו עמודות חדשות:

date_of_birth ו-customer_since בטבלת customers – ככל הנראה כדי לשמור מידע אישי נוסף.

currency ו-payment_method בטבלת payments – כדי לנהל עסקאות בינלאומיות ודרכי תשלום מגוונות.

מחיקת טבלאות (Dropping Tables)
שלוש טבלאות נמחקו:

mark_as_favorite

payment

devices

הוספת קשרי מפתח זר (Foreign Key Constraint)
הוספה של קשר מפתח זר (FOREIGN KEY) בין favorites.profile_id ל-profiles.profile_id, מה שמבטיח עקביות ושלמות נתונים (כל פרופיל שמופיע ב־favorites חייב להיות קיים בטבלת profiles).

### מבטים

מבט ראשון - מבט המציג לפרט כל לקוח עם תאריך תחילת המנוי ותאריך הלידה שלו לצד פרטי התוכנית: עלות חודשית, מדינה, מגבלת מכשירים, סוג התוכנית ומזהה התוכנית. שימושי לניתוח תמהיל מנויים לפי גיל, מדינה והגבלות מכשירים.

![image](https://github.com/user-attachments/assets/3e298139-9886-44de-998b-62f158c10760)



מבט שני - מבט המשלב נתונים מפרופילים, היסטוריית צפייה והעדפות (Favorites): תאריך צפייה, מזהה והמשך צפייה בסרט, שם הפרופיל, מצב מקוון, התאריך שבו נצפה סרט אהוב לאחרונה, מזהה הסרט האהוב וסך כל זמן הצפייה. שימושי לזיהוי משתמשים פעילים והעדפות תוכן.
![image](https://github.com/user-attachments/assets/8d2aadaf-8e59-4c6a-862f-f8417fefc73c)



שאילתות:
1. פרופילים שמחוברים כרגע
📜 תיאור מילולי:
שאילתה זו מציגה את שמות הפרופילים שמחוברים כרגע (is_online = TRUE) ואת סך כל זמן הצפייה שלהם. התוצאה ממוינת לפי תאריך הצפייה האחרון בסדר יורד.
```sql
SELECT 
    profile_name,
    total_time_watched
FROM 
    profile_view
WHERE 
    is_online = TRUE
ORDER BY 
    watch_date DESC;
```
![image](https://github.com/user-attachments/assets/3307d038-5bf9-4d10-a9b1-a3f5265c99df)

✅ 2. 40 המשתמשים שצפו הכי הרבה
📜 תיאור מילולי:
שאילתה המציגה את 40 הפרופילים שצפו הכי הרבה זמן בתוכן, כולל הסרט האהוב שלהם וזמן הצפייה האחרון. ממויין מהכי הרבה לצפייה הפחותה ביותר.
```sql
SELECT 
    profile_name,
    total_time_watched,
    favorite_movie_id,
    last_seen
FROM 
    profile_view
GROUP BY 
    profile_name, total_time_watched, favorite_movie_id, last_seen
ORDER BY 
    total_time_watched DESC
LIMIT 40;
```
![image](https://github.com/user-attachments/assets/5906d241-fbbd-4146-8573-0b598ba1f1af)

✅ 3. לקוחות ותיקים במיוחד
📜 תיאור מילולי:
שאילתה זו מאתרת לקוחות שהצטרפו לשירות עד לתאריך 1 בינואר 2005. היא כוללת את תאריך הלידה, מגבלת המכשירים, עלות המנוי וסוג התוכנית.
```sql
SELECT 
    customer_since,
    date_of_birth,
    device_limit,
    monthly_cost,
    plan_type
FROM 
    subscription_planner
WHERE 
    customer_since <= '2005-01-01'
ORDER BY 
    customer_since;
```
![image](https://github.com/user-attachments/assets/80b26fb6-6938-453a-9589-1359556ee9cd)


✅ 4. עלות לכל מכשיר (עלות חכמה)
📜 תיאור מילולי:
שאילתה זו מחשבת את יחס העלות החודשית למספר המכשירים בכל מנוי. תוצאה זו מאפשרת להבין אילו לקוחות מקבלים את הערך הגבוה ביותר (עלות נמוכה פר מכשיר). ממויין מהכי חסכוני.
```sql
SELECT 
    ROUND(monthly_cost / device_limit, 2) AS devices_cost_rate,
    customer_since,
    date_of_birth,
    device_limit,
    plan_id
FROM 
    subscription_planner
ORDER BY devices_cost_rate ASC
LIMIT 100;
```
![image](https://github.com/user-attachments/assets/6092c48f-0235-4a8a-8341-6626bbc0a555)



## תכנות postgresSQL

תוכנית 1:
התחלת התוכנית – הדפסת הודעת התחלה עם שם התוכנית והשעה הנוכחית.

שלב 1: קבלת סיכום לקוח – קריאה לפונקציה get_customer_summary עבור לקוח לפי customer_id, והצגת סיכום הכולל את שמו, מספר הפרופילים, דקות הצפייה ומספר התכנים שסימן כמועדפים.

שלב 2: עדכון מנוי – קריאה לפרוצדורה update_customer_subscription לעדכון תוכנית המנוי של הלקוח, כולל הנחה באחוזים.

סיכום התוכנית – הדפסת זמן הריצה של התוכנית.
```sql
-- main_program_1.sql
DO $$
DECLARE
    v_customer_id INTEGER := 1;
    v_new_plan_id INTEGER := 2;
    v_discount_percent INTEGER := 15;
    
    -- משתנים לפונקציה
    v_summary_record RECORD;
    
    -- משתנים כלליים
    v_start_time TIMESTAMP;
    v_program_name VARCHAR(50) := 'Customer Analysis Program';
BEGIN
    v_start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '=== % Started at % ===', v_program_name, v_start_time;
    
    -- חלק 1: קבלת סיכום לקוח עם הפונקציה
    RAISE NOTICE 'Step 1: Getting customer summary...';
    
    SELECT * INTO v_summary_record
    FROM get_customer_summary(v_customer_id);
    
    RAISE NOTICE 'Customer: %, Profiles: %, Watch Minutes: %, Favorites: %', 
                 v_summary_record.customer_name,
                 v_summary_record.total_profiles,
                 v_summary_record.total_watch_minutes,
                 v_summary_record.favorite_count;
    
    -- חלק 2: עדכון מנוי עם הפרוצדורה
    RAISE NOTICE 'Step 2: Updating customer subscription...';
    
    CALL update_customer_subscription(v_customer_id, v_new_plan_id, v_discount_percent);
    
    RAISE NOTICE 'Subscription updated successfully!';
    
    -- סיכום התוכנית
    RAISE NOTICE '=== % Completed in % seconds ===', 
                 v_program_name, 
                 EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - v_start_time));

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'ERROR in %: %', v_program_name, SQLERRM;
END $$;
```
![image](https://github.com/user-attachments/assets/3bda58f9-6371-434f-968d-7e91ce465008)
![image](https://github.com/user-attachments/assets/c9ce0ed1-db21-4e96-bbec-6913b855ddfb)




תוכנית 2:
התחלת התוכנית – הדפסת הודעת פתיחה עם שם התוכנית ושעת ההתחלה.

שלב 1: שליפת סרטים של הלקוח

קריאה לפונקציה get_customer_movies_cursor שמחזירה cursor עם רשימת סרטים של הלקוח.

קריאה מה־cursor בלולאה:

נספרים כל הסרטים.

מוצגים שלושת הסרטים הראשונים, כולל מזהה, משך צפייה, והאם סומן כמועדף.

סגירת ה־cursor בסיום.

שלב 2: העברת מועדפים בין פרופילים

קריאה לפרוצדורה transfer_favorites, שמעבירה עד movies_limit סרטים מועדפים מפרופיל אחד (מקור) לאחר (יעד), כאשר true מציין האם לאפשר דריסת נתונים קיימים (בהנחה שזה הפרמטר).

סיכום – הדפסת מספר הסרטים שנמצאו וזמן הריצה של התוכנית.

```sql
-- main_program_2.sql
DO $$
DECLARE
    v_customer_id INTEGER := 1;
    v_from_profile INTEGER := 1;
    v_to_profile INTEGER := 2;
    v_movies_limit INTEGER := 3;
    
    -- משתנים לעבודה עם cursor
    movies_cursor REFCURSOR;
    v_movie_record RECORD;
    v_movie_count INTEGER := 0;
    
    -- משתנים כלליים
    v_start_time TIMESTAMP;
    v_program_name VARCHAR(50) := 'Profile Management Program';
BEGIN
    v_start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '=== % Started at % ===', v_program_name, v_start_time;
    
    -- חלק 1: קבלת רשימת סרטים עם cursor
    RAISE NOTICE 'Step 1: Getting customer movies with cursor...';
    
    movies_cursor := get_customer_movies_cursor(v_customer_id);
    
    -- קריאה מה-cursor
    LOOP
        FETCH movies_cursor INTO v_movie_record;
        EXIT WHEN NOT FOUND;
        
        v_movie_count := v_movie_count + 1;
        
        -- הדפס רק 3 סרטים ראשונים
        IF v_movie_count <= 3 THEN
            RAISE NOTICE 'Movie %: ID=%, Minutes=%, Favorite=%', 
                         v_movie_count,
                         v_movie_record.movie_id,
                         v_movie_record.total_minutes,
                         v_movie_record.is_favorite;
        END IF;
    END LOOP;
    
    CLOSE movies_cursor;
    RAISE NOTICE 'Found % movies total', v_movie_count;
    
    -- חלק 2: העברת מועדפים בין פרופילים
    RAISE NOTICE 'Step 2: Transferring favorites between profiles...';
    
    CALL transfer_favorites(v_from_profile, v_to_profile, v_movies_limit, true);
    
    RAISE NOTICE 'Favorites transferred successfully!';
    
    -- סיכום התוכנית
    RAISE NOTICE '=== % Completed in % seconds ===', 
                 v_program_name,
                 EXTRACT(EPOCH FROM (CURRENT_TIMESTAMP - v_start_time));

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'ERROR in %: %', v_program_name, SQLERRM;
END $$;
```

![image](https://github.com/user-attachments/assets/d831a9ae-8964-433c-87d0-c28e7080b35d)
מצב התחלתי:
![image](https://github.com/user-attachments/assets/01d358ef-095b-415c-bb03-b009894c5f97)
![image](https://github.com/user-attachments/assets/98d1e0b1-9797-488b-af98-d6a11b203eeb)
הרצה:
![image](https://github.com/user-attachments/assets/3f0cc5b7-a68e-48db-89db-5ceb90e16dfc)

לאחר הרצה:

![image](https://github.com/user-attachments/assets/b7f42a95-d142-4db3-bbff-b547a85f0e0e)
![image](https://github.com/user-attachments/assets/ba3bca6f-9eca-4545-80d6-51897f223965)







## ממשק גרפי

הוראות כניסה למערכת:
כאשר מריצים את תוכנת המערכת, ייפתח חלון כפי שניתן לראות, ותתבקשו להכניס שם משתמש וסיסמא.
שם משתמש:  netflix_admin
סיסמא: password123
לאחר מכן לוחצים על login ונכנסים למערכת.



![image](https://github.com/user-attachments/assets/75f40924-8081-4e19-9f5b-c5397f531ed4)

### דרך העבודה:
 נתנו לבינה מלאכותית לייצר לנו שלבים לבניית הפרויקט. לאחר מכן, מימשנו את השלבים עם עזרה של Claude Sonnet 4. להלן השלבים:
 
 חיבור למסד נתונים
יצירת פונקציית חיבור (get_connection()) ל-PostgreSQL.

מסך התחברות
טופס פשוט שמוביל לתפריט הראשי.

תפריט ראשי
ניווט למסכים: לקוחות, פרופילים, היסטוריית צפייה, דוחות, יציאה.

מסך ניהול לקוחות (CRUD)
הצגה, הוספה, עדכון ומחיקה של לקוחות.

מסך ניהול פרופילים (CRUD)
עם קשר ללקוח (foreign key), כולל שדות סטטוס ותמונה.

מסך ניהול היסטוריית צפייה (CRUD)
טבלה מקשרת בין פרופילים לסרטים, עם צפייה ועדכון.

מסך דוחות ושאילתות
הרצת 2 שאילתות ו-2 פרוצדורות/פונקציות והצגת תוצאות.

שיפורים גרפיים ו-UX
יישור שדות, עיצוב נעים, הודעות משתמש, סרגלים וכפתורי ניווט.


### כלי הפיתוח:

שפת תכנות: Python

- שפת התכנות הראשית - קלה ללמידה, חזקה ונוחה לפיתוח GUI

- גרסה מומלצת: Python 3.8 ומעלה



ספרייה: Tkinter

- ספריית GUI המובנית של Python

- יתרונות: מגיעה עם Python, לא צריך התקנה נוספת

- שימוש: יצירת החלונות, הכפתורים, הטפסים והטבלאות





שפת שאילתות: PostgreSQL

- מסד נתונים רלציוני מתקדם ומקצועי

- יתרונות: חזק, אמין, תומך בשאילתות מורכבות

- שימוש: אחסון כל הנתונים של שירות הסטרימינג



ספרייה: psycopg2

- ספריית החיבור בין Python ל-PostgreSQL

- התקנה: pip install psycopg2

- שימוש: ביצוע שאילתות, עדכון נתונים, ניהול טרנזקציות




כלי הויזואליזציה:

- ספריית גרפים סטטיים - Matplotlib

- התקנה: pip install matplotlib

- שימוש: יצירת תרשימי עמודות של הכנסות חודשיות



ספריית ניתוח נתונים - Pandas

- התקנה: pip install pandas

- שימוש: עיבוד הנתונים לפני יצירת הגרפי


### תמונות מסך:


![queryA](https://github.com/user-attachments/assets/6c8ab236-eb91-4886-a69f-3a6fb2701d23)
![profiles_management](https://github.com/user-attachments/assets/fe61a7e9-0f7e-43f5-b4a1-147f3b2cea9c)
![procedure](https://github.com/user-attachments/assets/fa3c2d83-6b54-4f9e-a05f-28b78eda8aa7)
![main_menu](https://github.com/user-attachments/assets/04487efb-2f66-4be3-a1de-772163dc9f3a)
![login_window](https://github.com/user-attachments/assets/f846eb01-c5a3-40f0-8744-2d41fa550a72)
![login_successful](https://github.com/user-attachments/assets/d8465653-f186-4d03-8c3a-204db8da529a)
![insert_successful](https://github.com/user-attachments/assets/60bede9a-2ae3-4ab4-b3ae-33f4153cee59)
![function](https://github.com/user-attachments/assets/9fb16a80-45cd-4d13-9c85-0aee4414ba28)
![customers_management](https://github.com/user-attachments/assets/802056c2-c4ef-47c4-841a-d09db6368a80)
![watchhistory_management](https://github.com/user-attachments/assets/b5c02181-35de-4681-bbcf-022c8548463b)
![watch_history_management](https://github.com/user-attachments/assets/fdd95f86-7e4c-4fe7-b0a5-bee3c63b8423)
![revenue_chart](https://github.com/user-attachments/assets/61eac9fa-e8a2-4077-9b76-b4470126f90f)
![reports_window](https://github.com/user-attachments/assets/680f18e9-a0e2-417b-8fc4-03cbc807efb6)
![queryB](https://github.com/user-attachments/assets/7aceb871-31bc-4216-932b-bc98a6d9b970)
