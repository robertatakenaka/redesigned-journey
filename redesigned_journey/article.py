from opac_schema.v1.models import Article


def create_jsonl(get_data_function, output_jsonl_file_path):
    with open(output_jsonl_file_path, "w") as fp:
        fp.write("")

    items_per_page = 50
    page = 0
    while True:
        page += 1
        skip = ((page - 1) * items_per_page)
        limit = items_per_page
        items = Article.objects().skip(skip).limit(limit)
        try:
            items[0]
        except IndexError:
            break
        else:
            with open(output_jsonl_file_path, "a") as fp:
                data = "\n".join([get_data_function(item) for item in items])
                fp.write(f"{data}\n")
