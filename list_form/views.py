from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from list_form.utils import Valid_form, get_db_handle, find_forms


class HomePageView(View):
    def get(self, request):
        db = get_db_handle()
        context = list(
            map(lambda x: f'{x}</br>', db['forms'].find({}, {'_id': 0})))
        return HttpResponse(context)


class GetFormView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        context = {'result': ''}
        if request.method == 'POST':
            request_post = request.POST.copy()
            request_post.pop('csrfmiddlewaretoken', None)
            db = get_db_handle()

            if request_post:
                keys = request_post.keys()
                for key in keys:
                    request_post[key] = Valid_form(request_post[key]).type_form

                result_find = find_forms(db['forms'], request_post)
                result = [form['name'] for form in result_find]
                if result:
                    context['result'] = 'Имена подходящих форм:\n ' + \
                        '\n '.join(result)
                else:
                    context['result'] = 'Форма не найдена, по запросу должна быть такая форма \n{\n   '+',\n    '.join([f'{x}: {y}' for x, y in
                                                                                                                        request_post.items()])+'\n}'
            else:
                context['result'] = 'Для поиска форм необходимо передать не пустой запрос'
            return HttpResponse(context['result'])
