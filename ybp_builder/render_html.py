"""Generic code to render jinja template to html."""


from jinja2 import Environment, FileSystemLoader
import htmlmin

import posts


def render_template(template_path, template_fname, context):
    """Render the given template, using the Jinja engine."""
    template_environment = Environment(
        autoescape=False,
        loader=FileSystemLoader(template_path),
        trim_blocks=False
    )

    # TODO: standardize this
    context['post_mod'] = posts

    rendered = template_environment.get_template(
        template_fname
    ).render(context)

    return htmlmin.minify(rendered, remove_empty_space=True)


if __name__ == '__main__':
    import sys

    with open(sys.argv[3], 'w') as out_file:
        html = render_template(sys.argv[1], sys.argv[2], {})
        out_file.write(html.encode('utf-8'))
