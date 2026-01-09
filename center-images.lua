function Image (img)
  -- Add centering to images
  img.attr = img.attr or {}
  img.attr.attributes = img.attr.attributes or {}
  img.attr.attributes["custom-style"] = "Centered"
  return img
