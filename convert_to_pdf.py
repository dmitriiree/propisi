from fpdf import FPDF, XPos, YPos

class PDF(FPDF):
    def header(self):
        pass

def create_propisi_pdf():
    # Create instance of PDF class and add a page
    pdf = PDF()
    pdf.add_page()

    # Add the Propisi font and set it
    pdf.add_font("Propisi", "", "propisi.ttf")
    pdf.set_font("Propisi", size=26)

    # Set colors
    pdf.set_text_color(169, 169, 169)  # Gray text
    pdf.set_draw_color(169, 169, 169)  # Gray lines

    # Define measurements
    cell_height = 3  # Increased height for better spacing
    line_spacing = 3  # Space between lines
    margin_left = 10
    page_width = 210  # A4 page width
    margin_right = page_width - 10  # Right margin 10mm from edge
    start_y = 15
    num_lines = 2  # Number of lines for each text line
    page_height = 297  # A4 page height
    bottom_margin = 20  # Margin at the bottom of the page
    max_line_length = 80  # Increased maximum characters per line

    # Read and process the text from propisi.txt
    with open('propisi.txt', 'r', encoding='utf-8') as file:
        text_content = file.readlines()

    y = start_y
    for line in text_content:
        # Strip newline characters and remove empty lines
        line = line.strip()
        if not line:
            continue
        
        # Split long lines into multiple lines
        while len(line) > max_line_length:
            words = line.split()
            new_line = ""
            while words and len(new_line + words[0]) + 1 <= max_line_length:
                new_line += words.pop(0) + " "
            line = " ".join(words)
            
            # Check if we need to add a new page
            if y + cell_height + num_lines * line_spacing > page_height - bottom_margin:
                pdf.add_page()
                y = start_y  # Reset y position to the top of the page
            
            # Calculate the starting y position for the lines
            text_y = y + cell_height / 2 - 0.5
            
            # Set position and write text
            pdf.set_xy(margin_left, y)
            pdf.cell(margin_right - margin_left, cell_height, text=new_line.strip(), 
                    new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Draw multiple lines for propisi effect
            line_y = text_y
            for i in range(num_lines):
                pdf.line(margin_left, line_y + i * line_spacing, 
                        margin_right, line_y + i * line_spacing)
            
            # Increment y position for the next text line
            y += cell_height + num_lines * line_spacing

        # Check if we need to add a new page
        if y + cell_height + num_lines * line_spacing > page_height - bottom_margin:
            pdf.add_page()
            y = start_y  # Reset y position to the top of the page
        
        # Calculate the starting y position for the lines
        text_y = y + cell_height / 2 - 0.5
        
        # Set position and write text
        pdf.set_xy(margin_left, y)
        pdf.cell(margin_right - margin_left, cell_height, text=line, 
                new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Draw multiple lines for propisi effect
        line_y = text_y
        for i in range(num_lines):
            pdf.line(margin_left, line_y + i * line_spacing, 
                    margin_right, line_y + i * line_spacing)
        
        # Increment y position for the next text line
        y += cell_height + num_lines * line_spacing

    # Save the PDF
    pdf.output("propisi.pdf")

if __name__ == "__main__":
    create_propisi_pdf()
