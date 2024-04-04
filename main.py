
import flet as ft
import qrcode


def generate_qr(data, filename, ft_qrimage : ft.Image = None):
    qr = qrcode.make(data=data)
    qr.save(filename)

    
    if ft_qrimage:
        ft_qrimage.src = filename
        ft_qrimage.update()



generate_qr('test', filename='test.png')

def main(page : ft.Page):
    page.window_height = 400
    page.window_width = 400

    page.update()

    qr_data_input = ft.TextField(
        multiline=True, 
        max_lines=100, 
        expand=True,
        height=100,
        hint_text='QRcode data text, urls, etc.'
    )

    # add text label and qrdata input
    row_1 = ft.Row(
        controls = [
            ft.Text(value='QRCode Generator APP', size=25)
        ], 
        alignment = ft.MainAxisAlignment.CENTER
    )

    row_2 = ft.Row(
        controls=[qr_data_input], 
        alignment = ft.MainAxisAlignment.CENTER
    )

    # add qrcode image and file name text input and generae bt
    qr_image = ft.Image(
        src = 'test.png',
        height = 100,
        width = 100 
    )

    # add file name text input
    ft_file_name = ft.TextField(
        text_size=15,
        hint_text='QRcode image name',
        width=200
    )

    # add generate bt
    generate_bt = ft.ElevatedButton(
        text = 'Generate',
        bgcolor='blue',
        color='white',
        on_click = lambda e : generate_qr(
            qr_data_input.value, ft_file_name.value + '.png', qr_image)
    )


    row_3 = ft.Row(
        controls=[qr_image, ft_file_name], 
        alignment = ft.MainAxisAlignment.CENTER
    )

    row_4 = ft.Row(
        controls=[generate_bt], 
        alignment = ft.MainAxisAlignment.CENTER
    )



    page.add(row_1)
    page.add(row_2)
    page.add(row_3)
    page.add(row_4)

   


if __name__ == '__main__':
    ft.app(target = main)