import pandas as pd
import xlsxwriter
from io import BytesIO

def formatta_excel(file_csv_bytes):
    df = pd.read_csv(BytesIO(file_csv_bytes), header=None)
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet("Post Editoriali")

    blue = '#003DA5'
    light_gray = '#D3D3D3'

    label_format = workbook.add_format({
        'bold': True, 'font_color': blue, 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'bottom': 1, 'bottom_color': blue, 'align': 'center', 'valign': 'vcenter'
    })
    label_left = workbook.add_format({
        'bold': True, 'font_color': blue, 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'bottom': 1, 'bottom_color': blue, 'align': 'left', 'valign': 'vcenter'
    })
    label_bold_blue = workbook.add_format({
        'bold': True, 'font_color': blue, 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'align': 'center', 'valign': 'vcenter', 'bottom': 1, 'bottom_color': light_gray
    })
    cell_center = workbook.add_format({
        'font_color': 'black', 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'align': 'center', 'valign': 'vcenter', 'bottom': 1, 'bottom_color': light_gray
    })
    cell_left = workbook.add_format({
        'font_color': 'black', 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'align': 'left', 'valign': 'vcenter', 'bottom': 1, 'bottom_color': light_gray
    })
    header_format = workbook.add_format({
        'bold': True, 'font_color': 'black', 'font_name': 'Avenir Next LT Pro', 'font_size': 11,
        'align': 'center', 'valign': 'vcenter', 'bottom': 1, 'bottom_color': light_gray
    })

    worksheet.set_column("A:A", 82.5)
    worksheet.set_column("B:B", 13.83)
    worksheet.set_column("C:G", 6.83)
    worksheet.set_column("H:H", 7.5)

    row_pos = 0
    for _, row in df.iterrows():
        raw_values = row.tolist()
        is_header = (raw_values[0] == "Argomento")
        is_label = (
            not is_header and
            isinstance(raw_values[0], str) and
            raw_values[0] == raw_values[0].upper()
        )
        values = [
            "" if pd.isna(v) or str(v).strip().lower() in ["nan", "0"] else v
            for v in raw_values
        ]
        if all(v == "" for v in values):
            worksheet.set_row(row_pos, None)
            row_pos += 1
            continue

        for col, val in enumerate(values):
            if is_header:
                fmt = header_format
            elif is_label:
                fmt = label_left if col == 0 else label_format
            else:
                fmt = cell_left if col == 0 else (
                    label_bold_blue if col == 1 else cell_center
                )
            if val == "":
                worksheet.write_blank(row_pos, col, None, fmt)
            else:
                worksheet.write(row_pos, col, val, fmt)
        row_pos += 1

    workbook.close()
    output.seek(0)
    return output
