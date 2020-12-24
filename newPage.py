import helpers, os
import messages as msg

# settings = helpers.get_settings()

def execute(NAME):
    base = os.path.expanduser('~')
    cmd = 'mkdir ~/Documents/html'
    if os.path.isdir(base + '/Documents/html'):
        print("\nDirectory already exists. Moving on ...\n")
    else:
        print("\nCreating html directory ...\n")
        helpers.run_command(cmd)
    
    if os.path.isdir(base + '/Documents/html/css'):
        print("\nDirectory already exists. Moving on ...\n")
    else:
        print("\nCreating css directory ...\n")
        helpers.run_command(cmd)
    
    if os.path.isdir(base + '/Documents/html/js'):
        print("\nDirectory already exists. Moving on ...\n")
    else:
        print("\nCreating js directory ...\n")
        helpers.run_command(cmd)

    if os.path.exists(base + '/Documents/html/' + NAME + '.html'):
        print('File Already Exists\n')
    else:
        content = '''<!doctype html>
<html lang="en-US">
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" type="text/css" href="../segments/css/wc-segments.lib.min.css" />
        <script src="../segments/js/segments.lib.js"></script>
        <style>
            html,
            body,
            div,
            span,
            applet,
            object,
            iframe,
            h1,
            h2,
            h3,
            h4,
            h5,
            h6,
            p,
            blockquote,
            pre,
            a,
            abbr,
            acronym,
            address,
            big,
            cite,
            code,
            del,
            dfn,
            em,
            img,
            ins,
            kbd,
            q,
            s,
            samp,
            small,
            strike,
            strong,
            sub,
            sup,
            tt,
            var,
            dl,
            dt,
            dd,
            ol,
            ul,
            li,
            fieldset,
            form,
            label,
            legend,
            table,
            caption,
            tbody,
            tfoot,
            thead,
            tr,
            th,
            td {{
                margin: 0;
                padding: 0;
                border: 0;
                outline: 0;
                font-weight: inherit;
                font-style: inherit;
                font-family: inherit;
                font-size: 100%;
                vertical-align: baseline;
            }}
            body {{
                line-height: 1;
            }}
            ol,
            ul {{
                list-style: none;
            }}
            table {{
                border-collapse: separate;
                border-spacing: 0;
                vertical-align: middle;
            }}
            caption,
            th,
            td {{
                text-align: left;
                font-weight: normal;
                vertical-align: middle;
            }}
            a img {{
                border: none;
            }}
            body {{
                font-family: Helvetica Neue, arial, verdana, sans-serif;
                font-weight: 300;
                background-color: #444;
            }}
            panel-wrapper {{
                background-color: #fff;
            }}
            .left-justify {{
                text-align: left !important;
            }}
            .center-justify {{
                text-align: center !important;
            }}
            .right-justify {{
                text-align: right !important;
            }}
            .center {{
                margin: 0 auto;
            }}
            .left {{
                float: left;
            }}
            .right {{
                float: right;
            }}
            h1 {{
                font-size: 3.3rem;
                padding: 25px 0;
                line-height: 1.15;
            }}
            h2 {{
                padding: 20px 0;
                font-size: 2.5rem;
            }}
            h3 {{
                padding: 15px 0;
                font-size: 1.9rem;
            }}
            h4 {{
                font-size: 1.6rem;
            }}
            h5 {{
                font-size: 0.83rem;
            }}
            h6 {{
                font-size: 0.67rem;
            }}
            h4,
            h5 {{
                line-height: 1.3;
            }}
        </style>
        <title>{}</title>
    </head>
    <body>
    </body>
</html>'''.format(NAME.capitalize())

        helpers.run_command('mkdir ' + base + '/Documents/html/' + NAME)
        helpers.write_file(base + '/Documents/html/' + NAME + "/" + NAME + '.html', content)

    repoName = 'segments'
    
    if os.path.isdir(base + '/Documents/html/segments'):
        print("\nSegments already added. Moving on ...\n")
    else:
        print("\nGetting copy of segments ...\n")
        helpers.clone_repo(base + '/Documents/html', 'jaderigby', repoName)
    
    helpers.run_command('open -a "Google Chrome" "{}.html"'.format(base + '/Documents/html/' + NAME + "/" + NAME))

    print("\n[ Process Completed ]\n")
