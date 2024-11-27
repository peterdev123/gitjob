# tailwind classes
JOB_FIELD_COLOR = {
    'architecture_engineering': 'bg-blue-300',      # Steel Blue
    'arts_entertainment': 'bg-pink-200',            # Light Pink
    'business_management': 'bg-orange-200',         # Peach
    'communications': 'bg-sky-200',                 # Light Sky Blue
    'education': 'bg-yellow-200',                   # Light Gold
    'it': 'bg-green-300',                           # Yellow-Green
    'repair_maintenance': 'bg-red-200',             # Light Salmon
    'agriculture': 'bg-lime-200',                   # Pale Green
    'health_medicine': 'bg-rose-200',               # Light Coral
    'law_public_policy': 'bg-amber-200',            # Tan
    'sales': 'bg-yellow-300',                       # Gold
    'others': 'bg-gray-300',                        # Light Gray
}

def get_job_field_color(job_field):
    return JOB_FIELD_COLOR.get(job_field, 'bg-gray-300')    # returns the light gray as default