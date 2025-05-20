![image](https://github.com/user-attachments/assets/46c86656-68ee-4e11-87cc-beb47a4c1c71)# DBProject_330650680_216125815

**Submitters**:  
Shachar Levy – 330650680  
Yagel Kaniel – 216125815  

**System**: Streaming Service  
**Department**: Finances

---

## תוכן עניינים

1. [תיאור המערכת](#תיאור-המערכת)  
2. [מטרת המערכת](#מטרת-המערכת)  
3. [תיאור כללי](#תיאור-כללי)  
4. [מבנה הנתונים](#מבנה-הנתונים)  
5. [פונקציונליות עיקרית](#פונקציונליות-עיקרית)  
6. [תרשימים וצילומי מסך](#תרשימים-וצילומי-מסך)  
7. [שאילתות DELETE](#שאילתות-delete)  
8. [שאילתות UPDATE](#שאילתות-update)  
9. [שאילתות SELECT](#שאילתות-select)  
10. [תיאור ה-Constraints](#תיאור-ה-constraints)

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

## שאילתות DELETE

1. מחיקת הנחות שפג תוקפן ולא נעשה בהן שימוש:  
   ![image](https://github.com/user-attachments/assets/2ede949b-292a-41a9-ae1a-8a438f64556b)  
2. מחיקת מנויים שלא שילמו כלל:  
   ![image](https://github.com/user-attachments/assets/ef3ce8ba-890c-470e-ae37-04c7c906d5e2)  
3. מחיקת עסקאות שכשלו לפני יותר מחצי שנה:  
   ![image](https://github.com/user-attachments/assets/6510819a-7f9b-4cf3-b1be-a9d88446a26f)

---

## שאילתות UPDATE

1. עדכון סכום תשלום לפי אחוז הנחה:  
   ![image](https://github.com/user-attachments/assets/12b664fa-e586-4f0d-a76d-d731d4a8fec9)  
2. העלאת מחירי תוכניות בישראל ב־5%:  
   ![image](https://github.com/user-attachments/assets/b62cd1f4-fad7-48de-8d10-0f3dd4509b37)  
3. שינוי סטטוס עסקאות מ-Pending ל-Failed אחרי 7 ימים:  
   ![image](https://github.com/user-attachments/assets/609bea73-b4cb-4e52-9897-ad186decc665)

---

## שאילתות SELECT

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

## תיאור ה-Constraints

1. כמות מכשירים – בין 1 ל־9:  
   ![image](https://github.com/user-attachments/assets/7eb9cfda-db98-4f75-a22f-975171770e5e)  
2. שם הלקוח לא יכול להיות `NULL`:  
   ![image](https://github.com/user-attachments/assets/cf9f49fd-2d5d-419e-905a-0333c95e410a)  
3. סכום התשלום – בין 0 ל־9999.99:  
   ![image](https://github.com/user-attachments/assets/2941bf62-895e-4c30-8658-a0632eb703a1)

---

