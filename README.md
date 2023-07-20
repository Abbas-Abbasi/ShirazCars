# شیرازکارز - وبسایت لیستینگ خودرو آنلاین

شیرازکارز یک وبسایت لیستینگ خودرو آنلاین است که به کاربران امکان می‌دهد خودروهای خود را برای فروش لیست کنند. این وبسایت یک پلتفرم برای نمایش خودروها و برقراری ارتباط با خریداران پتانسیل فراهم می‌کند. وبسایت با استفاده از چارچوب پایتون Django ساخته شده است و شامل بسته‌های مختلفی برای افزایش قابلیت‌ها است.

## نصب

برای اجرای وبسایت شیرازکارز به صورت محلی، مراحل زیر را دنبال کنید:

1. کلون کردن مخزن:

   ```
   git clone https://github.com/Abbas-Abbasi/ShirazCars.git
   ```

2. وارد شدن به دایرکتوری پروژه:

   ```
   cd ShirazCars
   ```

3. ایجاد محیط مجازی:

   ```
   python3 -m venv myenv
   ```

4. فعالسازی محیط مجازی:

   - برای macOS/Linux:

     ```
     source myenv/bin/activate
     ```

   - برای Windows:

     ```
     myenv\Scripts\activate
     ```

5. نصب وابستگی‌های مورد نیاز:

   ```
   pip install -r requirements.txt
   ```

6. راه‌اندازی سرور توسعه:

   ```
   python manage.py runserver
   ```

7. مرورگر خود را باز کرده و به آدرس [http://localhost:8000](http://localhost:8000) مراجعه کنید تا به وبسایت شیرازکارز دسترسی پیدا کنید.

## استفاده

وبسایت شیرازکارز امکانات زیر را فراهم می‌کند:

- لیستینگ خودرو: کاربران می‌توانند لیستینگ‌های خود را برای خودروهای خود ایجاد کنند و جزئیاتی مانند سازنده، مدل، سال، قیمت و اطلاعات تماس را وارد کنند.
- جستجوی خودرو: کاربران می‌توانند براساس معیارهای خاصی مانند سازنده، مدل یا بازه قیمتی، خودروها را جستجو کنند.
- جزئیات خودرو: هر لیستینگ خودرو شامل اطلاعات دقیقی درباره خودرو است، از جمله عکس‌ها، مشخصات و جزئیات تماس فروشنده.
- ثبت نام و احراز هویت کاربران: کاربران می‌توانند ثبت‌نام کنند، وارد شوند و حساب کاربری خود را مدیریت کنند. این به آن‌ها امکان می‌دهد تا لیستینگ‌های خودروی خود را ایجاد و مدیریت کنند.
- داشبورد کاربر: کاربران ثبت‌نام شده به یک داشبورد دسترسی دارند که در آن می‌توانند لیستینگ‌های خودروی خود را مشاهده، ویرایش و حذف کنند.

## پیکربندی

تنظیمات پروژه Django در فایل `settings.py` قابل یافتن است. این فایل شامل تنظیمات مربوط به پایگاه داده، فایل‌های استاتیک، بارگذاری رسانه، احراز هویت و سایر تنظیمات مربوط به پروژه است. شما می‌توانید این فایل را براساس نیازهای خود تغییر دهید.

## بسته‌های استفاده شده

وبسایت شیرازکارز از بسته‌های زیر استفاده می‌کند:

- asgiref
- autopep8
- boto3
- botocore
- Django~=4.2.2
- django-crispy-forms
- django-environ
- django-filter~=23.2
- django-localflavor
- django-storages
- gunicorn
- jmespath
- Pillow
- psycopg2
- pycodestyle
- python-dateutil
- python-stdnum
- s3transfer
- six
- sqlparse
- toml
- urllib3
- whitenoise
- environ~=1.0

## همکاری

همکاری در این پروژه مورد استقبال قرار می‌گیرد. اگر می‌خواهید همکاری کنید، لطفاً مراحل زیر را دنبال کنید:

1. فورک کردن مخزن در GitHub.
2

. ایجاد یک شاخه جدید با نام توصیفی.
3. پیاده‌سازی تغییرات یا اضافه کردن ویژگی‌های جدید.
4. اعمال تغییرات خود با پیام‌های واضح و مختصر.
5. ارسال شاخه خود به مخزن فورک شده.
6. ارسال درخواست pull که تغییرات شما و مزایای آن را توضیح می‌دهد.

## مجوز

این پروژه تحت مجوز [مجوز MIT](LICENSE.md) ارائه می‌شود.

## قدردانی

- این وبسایت با تمرکز بر سادگی و ارائه یک پلتفرم کاربرپسند برای لیستینگ و فروش خودروها ساخته شده است.
- تشکر ویژه از انجمن Django برای چارچوب برتر آن و بسته‌های مختلف استفاده شده جهت افزایش قابلیت‌های وبسایت.


------------------------------------------------------------

# ShirazCars - Online Car Listing Website

ShirazCars is an online car listing website that allows users to list their cars for sale. It provides a platform for users to showcase their vehicles and connect with potential buyers. The website is built using Python Django framework and includes various packages for enhanced functionality.

## Installation

To run the ShirazCars website locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Abbas-Abbasi/ShirazCars.git
   ```

2. Navigate to the project directory:

   ```
   cd ShirazCars
   ```

3. Create a virtual environment:

   ```
   python3 -m venv myenv
   ```

4. Activate the virtual environment:

   - For macOS/Linux:

     ```
     source myenv/bin/activate
     ```

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

7. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the ShirazCars website.

## Usage

The ShirazCars website provides the following features:

- Car Listing: Users can create listings for their cars, providing details such as make, model, year, price, and contact information.
- Car Search: Users can search for cars based on specific criteria, such as make, model, or price range.
- Car Details: Each car listing includes detailed information about the vehicle, including photos, specifications, and seller contact details.
- User Registration and Authentication: Users can register, log in, and manage their accounts. This allows them to create and manage their car listings.
- User Dashboard: Registered users have access to a dashboard where they can view, edit, and delete their car listings.

## Configuration

The configuration for the Django project can be found in the `settings.py` file. It includes settings for database configuration, static files, media uploads, authentication, and other project-specific settings. You may modify this file as per your requirements.

## Packages Used

The ShirazCars website utilizes the following packages:

- asgiref
- autopep8
- boto3
- botocore
- Django~=4.2.2
- django-crispy-forms
- django-environ
- django-filter~=23.2
- django-localflavor
- django-storages
- gunicorn
- jmespath
- Pillow
- psycopg2
- pycodestyle
- python-dateutil
- python-stdnum
- s3transfer
- six
- sqlparse
- toml
- urllib3
- whitenoise
- environ~=1.0

## Contributing

Contributions to this project are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Implement your changes or add new features.
4. Commit your changes with clear and concise commit messages.
5. Push your branch to your forked repository.
6. Submit a pull request, describing your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- This website was built with a focus on simplicity and providing a user-friendly platform for car listings and sales.
- Special thanks to the Django community for their excellent framework and the various packages used to enhance the functionality of the website.
