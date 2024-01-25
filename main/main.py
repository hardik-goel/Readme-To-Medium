from conf.configs import readme_path, API_KEY, MODEL_NAME, output_file_path_for_images
from utils.publish import execute
from utils.scrape import scrape_github_readme
from utils.rephrase import initialise_model, rephrase_text


contents = scrape_github_readme(readme_path, output_file_path_for_images)
model = initialise_model(API_KEY,MODEL_NAME)
output_file_path = rephrase_text(contents,model)
execute(output_file_path)