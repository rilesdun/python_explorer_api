"""
Script to convert a JSON file bandit report to an HTML file
"""
import json

def json_to_html(input_file, output_file):
    """
    Function to convert a JSON file to an HTML file
    """
    with open(input_file, 'r', encoding='utf-8') as f: # pylint: disable=invalid-name
        data = json.load(f)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bandit Report</title>
    </head>
    <body>
        <h1>Bandit Scan Report</h1>
        <h2>Metrics</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>File</th>
                    <th>Lines of Code</th>
                    <th>Skipped Tests</th>
                    <th>Confidence High</th>
                    <th>Confidence Low</th>
                    <th>Confidence Medium</th>
                    <th>Confidence Undefined</th>
                    <th>Severity High</th>
                    <th>Severity Low</th>
                    <th>Severity Medium</th>
                    <th>Severity Undefined</th>
                    <th>Nosec</th>
                </tr>
            </thead>
            <tbody>
    """

    for file, metrics in data['metrics'].items():
        html_content += f"""
        <tr>
            <td>{file}</td>
            <td>{metrics['loc']}</td>
            <td>{metrics['skipped_tests']}</td>
            <td>{metrics['CONFIDENCE.HIGH']}</td>
            <td>{metrics['CONFIDENCE.LOW']}</td>
            <td>{metrics['CONFIDENCE.MEDIUM']}</td>
            <td>{metrics['CONFIDENCE.UNDEFINED']}</td>
            <td>{metrics['SEVERITY.HIGH']}</td>
            <td>{metrics['SEVERITY.LOW']}</td>
            <td>{metrics['SEVERITY.MEDIUM']}</td>
            <td>{metrics['SEVERITY.UNDEFINED']}</td>
            <td>{metrics['nosec']}</td>
        </tr>
        """

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as f: # pylint: disable=invalid-name
        f.write(html_content)

if __name__ == "__main__":
    json_to_html('bandit-security-report/bandit-report.json', 'bandit-security-report/index.html')
