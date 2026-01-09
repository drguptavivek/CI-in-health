-- pagebreak.lua
-- Inserts a page break before each level-1 header (chapter)
local pagebreak_latex = pandoc.RawBlock('latex', '\\newpage')
local pagebreak_ooxml = pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>')
local first_header = true
function Header(el)
  if el.level == 1 then
    if first_header then
      -- Don't add page break before the very first header
      first_header = false
      return el
    else
      -- Add page break before subsequent level-1 headers
      if FORMAT:match 'latex' or FORMAT:match 'pdf' then
        return {pagebreak_latex, el}
      elseif FORMAT:match 'docx' or FORMAT:match 'odt' then
        return {pagebreak_ooxml, el}
      else
        return el
      end
    end
  end
  return el
end
