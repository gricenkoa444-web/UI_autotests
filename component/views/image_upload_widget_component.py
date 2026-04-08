from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.views.empty_view_component import EmptyViewComponent
from element.button import Button
from element.file_input import FileInput
from element.icon import Icon
from element.image import Image
from element.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        #create-course-preview
        self.image_preview = Image(
            page, f"{identifier}-image-upload-widget-preview-image", "Image preview"
        )

        self.image_upload_info_icon = Icon(
            page, f"{identifier}-image-upload-widget-info-icon", "Upload info icon"
        )
        self.image_upload_info_title = Text(
            page, f"{identifier}-image-upload-widget-info-title-text", "Upload info title"
        )
        self.image_upload_info_description = Text(
           page, f"{identifier}-image-upload-widget-info-description-text", "Upload info description"
        )
        self.upload_button = Button(
            page, f"{identifier}-image-upload-widget-upload-button", "Upload image button"
        )
        self.remove_button = Button(
            page, f"{identifier}-image-upload-widget-remove-button", "Remove image button"
        )
        self.input_button = FileInput(
            page, f"{identifier}-image-upload-widget-input", "Input for upload image"
        )


    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()

        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.upload_button.check_visible()

        if is_image_uploaded:
            self.remove_button.check_visible()
            self.image_preview.check_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here"
            )

    def click_remove(self):
        self.remove_button.click()

    def upload_image(self, file: str):
        self.input_button.set_input_files(file)
