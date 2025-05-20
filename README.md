# DBProject_330650680_216125815
Submitters:
Shachar Levy 330650680
Yagel Kaniel 216125815
System: Streaming Service
Dept.: Finances

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

תוכן עניינים:

תיאור המערכת

מטרת המערכת

תיאור כללי

מבנה הנתונים

פונקציונליות עיקרית

תרשימים וצילומי מסך

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

מטרת המערכת:
המערכת נועדה לנהל את שירותי המנויים של פלטפורמת סטרימינג, תוך מעקב אחר תשלומים, החזרים, הנחות ועסקאות כספיות. המערכת מאפשרת לשמור מידע על תוכניות מנוי, לנהל תהליכי חיוב אוטומטיים ולבצע החזרים במקרה הצורך.

הנתונים הנשמרים במערכת:
תוכניות מנוי (Subscription_Plans) – רשימת התוכניות השונות הקיימות, כולל סוג התוכנית (Basic, Standard, Premium), תקופת המנוי (חודשי, חצי שנתי, שנתי) והעלות החודשית.

מנויים (Subscriptions) – לקוחות רשומים הכוללים את פרטיהם האישיים, תוכנית המנוי אליה הם מחוברים והנחות שהם מקבלים.

הנחות ומבצעים (Discounts) – הנחות זמינות למנויים, כולל גובה ההנחה ותוקף המבצע.

תשלומים (Payments) – פרטי תשלומים שבוצעו על ידי המנויים, כולל סכום ותאריך התשלום.

החזרים (Refunds) – החזרים כספיים שניתנו למנויים, כולל סכום ההחזר והתאריך בו בוצע.

עסקאות (Transactions) – מצב העסקאות הקשורות לתשלומים, כולל הצלחה, כשלון או המתנה, ותאריך ביצוע העסקה.

פונקציונליות עיקרית במערכת:
✔️ רישום מנויים ושיוכם לתוכנית מנוי מסוימת.
✔️ חישוב תשלומים אוטומטי בהתאם לתוכנית המנוי וההנחות הזמינות.
✔️ מעקב אחר סטטוס עסקאות ותשלומים שבוצעו.
✔️ טיפול בהחזרים למנויים במקרה של ביטול מנוי או בעיה בחיוב.
✔️ ניהול מבצעים והנחות, כולל תוקף וזכאות להנחה.
✔️ הפקת דוחות על הכנסות, תשלומים והחזרים לצורכי מעקב וניתוח כלכלי.

המערכת מאפשרת לפלטפורמת הסטרימינג לנהל את הצד הפיננסי שלה בצורה מסודרת ויעילה, תוך שמירה על מידע מדויק וניהול עסקאות בצורה חלקה.

![image](https://github.com/user-attachments/assets/4c3cecd1-efd8-46eb-bae7-523498f0f170)
![image](https://github.com/user-attachments/assets/8d1ce340-d550-4fc4-ada1-38ff7af66083)
![image](https://github.com/user-attachments/assets/e0bb848e-2f1a-407a-8018-e620753e0973)
![image](https://github.com/user-attachments/assets/a22914ed-d72d-4c6d-82c1-f003f5614e7b)
![image](https://github.com/user-attachments/assets/7beb71cf-4c5d-407a-86f2-e44a2704af32)
![image](https://github.com/user-attachments/assets/83b18cf8-9bde-4290-9a6e-36c4127fc4bb)
![image](https://github.com/user-attachments/assets/35930a9b-7191-41bf-b678-ad44dab563bc)
![image](https://github.com/user-attachments/assets/c4bbdce4-cd57-4d95-8fd3-c1d089703def)
![image](https://github.com/user-attachments/assets/cade33d3-9810-4167-96e8-352db5c68d41)
![image](https://github.com/user-attachments/assets/5c008d18-c070-48d8-91fa-505cd7efc411)
![image](https://github.com/user-attachments/assets/2f9983a4-08f8-42ce-b2ad-91727a1dc018)

שאילתות delete
1. השאילתה מוחקת מהטבלה discounts את כל ההנחות שתוקפן פג לפני יותר משנה, ושלא נעשה בהן שימוש על ידי אף מנוי (כלומר, אין אף רשומה בטבלת subscriptions שבה מופיעה אותה discount_id).

![image](https://github.com/user-attachments/assets/2ede949b-292a-41a9-ae1a-8a438f64556b)
![image](https://github.com/user-attachments/assets/cb1777e1-3755-43cd-baaa-62bd80af9a7d)
![image](https://github.com/user-attachments/assets/71a514aa-ad85-45ce-a774-6842d85531ff)
![image](https://github.com/user-attachments/assets/3143fe93-65ae-40ab-a1e7-23a3926ae416)
2. השאילתה מוחקת מהטבלה subscriptions את כל המנויים שלא בוצע עבורם אף תשלום — כלומר, כאלה שאין להם רשומות מתאימות בטבלת payments.

![image](https://github.com/user-attachments/assets/ef3ce8ba-890c-470e-ae37-04c7c906d5e2)
![image](https://github.com/user-attachments/assets/b554ae2a-a423-4070-84fc-7e833a4e7dde)
![image](https://github.com/user-attachments/assets/9f8f1c90-a3fe-4c3b-a747-163a6c37a7a8)
![image](https://github.com/user-attachments/assets/6adfc7a2-604e-496a-bee2-9e422e041c0f)

3. השאילתה מוחקת מהטבלה transactions את כל העסקאות שכשלו (status = 'Failed') ושהתרחשו לפני יותר מחצי שנה.
![image](https://github.com/user-attachments/assets/6510819a-7f9b-4cf3-b1be-a9d88446a26f)
![image](https://github.com/user-attachments/assets/8bc90fec-1d08-4543-8387-364615325dcc)
![image](https://github.com/user-attachments/assets/14e70572-906e-4473-8bf0-d5e3775d3931)
![image](https://github.com/user-attachments/assets/18d72d2e-03c3-4c1c-9942-6292dcd33ed9)

שאילתות update
1. השאילתה מעדכנת את הסכום (amount) בטבלת payments, כך שישקף את ההנחה הרלוונטית: היא מחשבת את הסכום לאחר הנחה לפי האחוז (discount_percent) מתוך טבלת discounts.
העדכון מתבצע רק עבור תשלומים שמקושרים למנויים שיש להם הנחה בתוקף (כלומר, שהשדה valid_until בתאריך הנוכחי או מאוחר ממנו).
![image](https://github.com/user-attachments/assets/12b664fa-e586-4f0d-a76d-d731d4a8fec9)
![image](https://github.com/user-attachments/assets/59288430-c274-45f0-b6cd-2c2c3d44b7c7)
![image](https://github.com/user-attachments/assets/04fc28bf-8ccd-4fd0-8cb4-dcae82d02b97)
![image](https://github.com/user-attachments/assets/3b67a677-312d-4ff0-b193-7ab55d2795dd)


2.   השאילתה מעדכנת את טבלת subscription_plans ומעלה את המחיר החודשי (monthly_cost) ב־5% לכל התוכניות שמיועדות לישראל (country = 'Israel').
המחיר המעודכן מעוגל לשתי ספרות אחרי הנקודה.

![image](https://github.com/user-attachments/assets/b62cd1f4-fad7-48de-8d10-0f3dd4509b37)
![image](https://github.com/user-attachments/assets/ced02bce-c0a3-4a3e-ac33-3dc597b0c847)
![image](https://github.com/user-attachments/assets/04fc28bf-8ccd-4fd0-8cb4-dcae82d02b97)
![image](https://github.com/user-attachments/assets/279aa45c-ce02-4e1e-affe-6a6df5981b80)

3. השאילתה מעדכנת את טבלת transactions ומשנה את הסטטוס של עסקאות שתלויות (status = 'Pending') ל־Failed, אם עברו יותר משבעה ימים ממועד ביצוע העסקה (transaction_date).
   
![image](https://github.com/user-attachments/assets/609bea73-b4cb-4e52-9897-ad186decc665)
![image](https://github.com/user-attachments/assets/8445278a-6a96-498c-a61c-e0341bdd84c9)
![image](https://github.com/user-attachments/assets/b3326b0f-f24d-4f89-83b3-d67c192889b7)
![image](https://github.com/user-attachments/assets/ae2705fb-bfa6-4268-a50b-26e2e162df4a)

שאילתות select
1. שאילתה זו מחשבת סך תשלומים חודשיים לאחר הנחות ומדרגת אותם לפי גובה ההכנסה. תחילה, היא מחשבת את הסכום המופחת לכל תשלום בהתאם להנחות הרלוונטיות. אחר כך, היא מקבצת את הנתונים לפי חודש ושנה ומסכמת את התשלומים בכל חודש. לבסוף, השאילתה מדרגת את החודשים לפי גובה ההכנסות בסדר יורד.
   WITH DiscountedPayments AS (
  SELECT 
    p.payment_date,
    -- Apply discount if it exists, else use full amount
    p.amount * (1 - COALESCE(d.discount_percent, 0) / 100.0) AS discounted_amount
  FROM Payments p
  JOIN Subscriptions s ON p.subscription_id = s.subscription_id
  LEFT JOIN Discounts d ON s.discount_id = d.discount_id
),
MonthlyPayments AS (
  SELECT 
    EXTRACT(YEAR FROM payment_date) AS year,
    EXTRACT(MONTH FROM payment_date) AS month,
    SUM(discounted_amount) AS total_monthly_amount
  FROM DiscountedPayments
  GROUP BY year, month
),
RankedPayments AS (
  SELECT 
    year,
    month,
    total_monthly_amount,
    RANK() OVER (ORDER BY total_monthly_amount DESC) AS sales_rank
  FROM MonthlyPayments
)
SELECT *
FROM RankedPayments
ORDER BY total_monthly_amount DESC
LIMIT 40;

![image](https://github.com/user-attachments/assets/bce46179-c9e4-4289-b61f-fbc0a2c71264)
2. שאילתה זו מחשבת את סוג המנוי (plan_type) שהניב את ההכנסה הגבוהה ביותר בכל שנה, תוך התחשבות בהנחות.
SELECT year, plan_type, total_revenue
FROM (
    SELECT 
        EXTRACT(YEAR FROM p.payment_date) AS year,
        sp.plan_type,
        SUM(p.amount * (1 - COALESCE(d.discount_percent, 0) / 100.0)) AS total_revenue,
        RANK() OVER (
            PARTITION BY EXTRACT(YEAR FROM p.payment_date)
            ORDER BY SUM(p.amount * (1 - COALESCE(d.discount_percent, 0) / 100.0)) DESC
        ) AS rnk
    FROM Payments p
    JOIN Subscriptions s ON p.subscription_id = s.subscription_id
    JOIN Subscription_Plans sp ON s.plan_id = sp.plan_id
    LEFT JOIN Discounts d ON s.discount_id = d.discount_id
    GROUP BY year, sp.plan_type
) AS ranked
WHERE rnk = 1
ORDER BY year;
![image](https://github.com/user-attachments/assets/f180b158-64fb-4868-9526-490deec418e6)

3. שאילתה זו מנתחת את היחס בין העלות הממוצעת של מנוי לאחר הנחות לבין מספר המנויים בכל מדינה.
SELECT 
  sp.country,
  AVG(sp.monthly_cost * (1 - COALESCE(d.discount_percent, 0) / 100.0)) AS avg_discounted_cost,
  COUNT(s.subscription_id) AS subscription_count,
  AVG(sp.monthly_cost * (1 - COALESCE(d.discount_percent, 0) / 100.0)) / COUNT(s.subscription_id) AS subscription_count_revenue_ratio


FROM Subscription_Plans sp
JOIN Subscriptions s ON sp.plan_id = s.plan_id 
LEFT JOIN Discounts d ON s.discount_id = d.discount_id
GROUP BY sp.country
ORDER BY subscription_count_revenue_ratio

 DESC;
![image](https://github.com/user-attachments/assets/516b399b-0000-4cb8-a3ee-e3c62ec4bc3d)

4. שאילתה זו מנתחת את היחס בין ההכנסה הממוצעת לכמות המנויים בכל מדינה, ומסדרת את התוצאות מהיחס הגבוה לנמוך.
   ![image](https://github.com/user-attachments/assets/404b62c7-5358-4661-841d-8e747c3dd906)


תיאור ה constraints:
1. כמות המכשירים גדולה מ 0 וקטנה מ 10.
![image](https://github.com/user-attachments/assets/7eb9cfda-db98-4f75-a22f-975171770e5e)


2. שם הלקוח לא יכול להיות "null"
   ![image](https://github.com/user-attachments/assets/cf9f49fd-2d5d-419e-905a-0333c95e410a)



3. כמות התשלום גדולה מ 0 וקטנה מ 9999.99
![image](https://github.com/user-attachments/assets/2941bf62-895e-4c30-8658-a0632eb703a1)






