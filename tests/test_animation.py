import os
from playwright.sync_api import Page, expect

def test_card_animation_on_mobile(page: Page):
    """
    Tests that the card expands on click on a mobile viewport.
    """
    # Set a mobile viewport
    page.set_viewport_size({"width": 500, "height": 800})

    # Navigate to the local index.html file
    path = "file://" + os.path.abspath("index.html")
    page.goto(path)

    card = page.locator("#card")

    # Get the initial height of the card
    initial_box = card.bounding_box()
    assert initial_box is not None, "Card should be visible initially."

    # Click the card to trigger the animation
    card.click()

    # Wait for the animation to complete (transition is 0.4s)
    page.wait_for_timeout(500)

    # Get the final height of the card
    final_box = card.bounding_box()
    assert final_box is not None, "Card should be visible after click."

    # Assert that the card's height has increased
    assert final_box['height'] > initial_box['height'], "The card should expand on click."

    # Assert that the card has the 'hovered' class
    expect(card).to_have_class("card hovered")