from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        #create-course-preview
        self.image_preview = page.get_by_test_id(f"{identifier}-image-upload-widget-preview-image")

        self.image_upload_info_icon = page.get_by_test_id(f"{identifier}-image-upload-widget-info-icon")
        self.image_upload_info_title = page.get_by_test_id(f"{identifier}-image-upload-widget-info-title-text")
        self.image_upload_info_description = page.get_by_test_id(
            f"{identifier}-image-upload-widget-info-description-text"
        )
        self.upload_button = page.get_by_test_id(f"{identifier}-image-upload-widget-upload-button")
        self.remove_button = page.get_by_test_id(f"{identifier}-image-upload-widget-remove-button")
        self.input_button = page.get_by_test_id(f"{identifier}-image-upload-widget-input")


    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_info_icon).to_be_visible()

        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')

        expect(self.upload_button).to_be_visible()

        if is_image_uploaded:
            expect(self.remove_button).to_be_visible()
            expect(self.image_preview).to_be_visible()

        if not is_image_uploaded:
            self.preview_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here"
            )

    def click_remove(self):
        self.remove_button.click()

    def upload_image(self, file: str):
        self.input_button.set_input_files(file)
