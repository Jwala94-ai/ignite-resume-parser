"""Layout detection for resume sections"""
class LayoutDetector:
    
    def detect(self, text):

        lines = text.split("\n")

        avg_line_length = sum(
            len(line)
            for line in lines
        ) / max(len(lines),1)

        if avg_line_length < 40:
            return "multi-column"

        return "single-column"