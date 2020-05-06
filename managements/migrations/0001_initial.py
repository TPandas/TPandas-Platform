# Generated by Django 3.0.5 on 2020-05-06 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ByTypeModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='定位器类型ID')),
                ('by_locator_type', models.CharField(max_length=40, verbose_name='定位器类型名称')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CaseModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='用例ID')),
                ('module_name', models.CharField(max_length=20, verbose_name='模块名称')),
                ('kit_name', models.CharField(max_length=20, verbose_name='套件名称')),
                ('case_name', models.CharField(max_length=20, verbose_name='用例名称')),
                ('case_status', models.IntegerField(verbose_name='用例状态（0：停用，1：启用）')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnvModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='环境ID')),
                ('name', models.CharField(max_length=30, verbose_name='环境名称')),
                ('desc', models.TextField(verbose_name='环境描述')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='项目ID')),
                ('name', models.CharField(max_length=40, verbose_name='项目名称')),
                ('status', models.IntegerField(verbose_name='项目状态(0：未开始，1：进行中，2：已完成，3：阻塞，4：关闭)')),
                ('desc', models.TextField(verbose_name='项目描述')),
                ('start_time', models.DateTimeField(verbose_name='项目开始时间')),
                ('end_time', models.DateTimeField(verbose_name='项目结束时间')),
                ('leader', models.CharField(max_length=40, verbose_name='项目负责人')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestDataModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='测试数据ID')),
                ('data_name', models.CharField(max_length=20, verbose_name='数据名称')),
                ('test_data', models.TextField(verbose_name='测试数据')),
                ('data_tag', models.IntegerField(verbose_name='数据标记（0：不处理，1：删除）')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.CaseModel', verbose_name='测试用例')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.EnvModel', verbose_name='项目环境')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PageObjectModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='元素ID')),
                ('page_name', models.CharField(max_length=20, verbose_name='页面名称')),
                ('model_name', models.CharField(max_length=20, verbose_name='功能模块名称')),
                ('obj_name', models.CharField(max_length=40, verbose_name='元素名称')),
                ('by_locator', models.CharField(max_length=255, verbose_name='元素定位器内容')),
                ('by_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.ByTypeModel', verbose_name='定位类型')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GlobalsDataModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=40, verbose_name='Globals name')),
                ('value', models.CharField(max_length=40, verbose_name='Globals value')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.EnvModel', verbose_name='项目环境')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='casemodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.ProjectModel', verbose_name='所属项目'),
        ),
        migrations.CreateModel(
            name='CaseDateModel',
            fields=[
                ('create_auth', models.CharField(max_length=20, verbose_name='创建者')),
                ('update_auth', models.CharField(max_length=20, verbose_name='修改者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('id', models.AutoField(db_index=True, primary_key=True, serialize=False, verbose_name='测试用例与测试数据关联表')),
                ('test_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.CaseModel')),
                ('test_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managements.TestDataModel')),
            ],
            options={
                'verbose_name': '公共字段',
                'abstract': False,
            },
        ),
    ]
