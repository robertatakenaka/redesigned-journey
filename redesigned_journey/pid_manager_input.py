import os
import argparse
import json

from redesigned_journey.article import create_jsonl
from redesigned_journey.db import db_connect_by_uri


def get_row_data(doc):
    v2 = doc.pid
    v3 = doc._id
    aop = doc.aop_pid
    doi = doc.doi.upper()
    pub_year = doc.publication_date[:4]
    issue_order = str(doc.issue.order).zfill(4)
    elocation = doc.elocation
    fpage = doc.fpage
    lpage = doc.lpage
    article_title = doc.title.upper()

    try:
        other_pids = " ".join(doc.scielo_pids['other'])
    except (KeyError, TypeError, ValueError):
        other_pids = ""

    try:
        filename = doc.pdfs[0]['filename']
    except (IndexError, KeyError, AttributeError):
        filename = ""
    else:
        name, ext = os.path.splitext(filename)
        filename = name + ".xml"

    try:
        first_author_surname = doc.authors[0].split(",")[0].upper()
    except IndexError:
        first_author_surname = ""
    try:
        last_author_surname = doc.authors[-1].split(",")[0].upper()
    except IndexError:
        last_author_surname = ""

    names = (
        'v2', 'v3', 'aop', 'filename', 'doi',
        'pub_year', 'issue_order', 'elocation', 'fpage', 'lpage',
        'first_author_surname', 'last_author_surname',
        'article_title', 'other_pids',
        'status',
    )
    values = (
        v2, v3, aop, filename, doi,
        pub_year, issue_order, elocation, fpage, lpage,
        first_author_surname, last_author_surname,
        article_title, other_pids,
        'published' if doc.is_public else 'not_published',
    )
    return json.dumps(dict(zip(names, values)))


def main():
    parser = argparse.ArgumentParser(description="Data extractor")
    subparsers = parser.add_subparsers(
        title="Commands", metavar="", dest="command",
    )

    get_parser = subparsers.add_parser(
        "get",
        help=(
            "Get data from website"
        )
    )
    get_parser.add_argument(
        "db_uri",
        help=(
            "mongodb://{login}:{password}@{host}:{port}/{database}"
        )
    )
    get_parser.add_argument(
        "output_jsonl_file_path",
        help=(
            "/path/documents.jsonl"
        )
    )

    args = parser.parse_args()
    if args.command == "get":
        db_connect_by_uri(args.db_uri)

        create_jsonl(get_row_data, args.output_jsonl_file_path)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
