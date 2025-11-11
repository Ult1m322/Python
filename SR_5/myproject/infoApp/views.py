from django.http import HttpResponse

def student_info(request):
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Інформація про студента</title>
        </head>
        <body>
            <h1>Інформація про студента</h1>
            <table border="1">
                <tr>
                    <td>Прізвище</td>
                    <td>Кішко</td>
                </tr>
                <tr>
                   <td>Ім'я </td>   
                   <td>Олексій </td> 
                </tr>
                <tr>
                    <td>Група</td>
                    <td>ІСД-32</td>
                </tr>
            </table>
        </body>
    </html>
    """
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')
