"""
Schema list
"""
abstartups_schema = [
  { "name": "name", "type": "STRING" },
  { "name": "founded_at", "type": "STRING" },
  { "name": "created_at", "type": "STRING" },
  { "name": "short_description", "type": "STRING" },
  { "name": "description", "type": "STRING" },
  { "name": "slug", "type": "STRING" },
  { "name": "profile_image", "type": "STRING" },
  { "name": "is_verified", "type": "STRING" },
  { "name": "employees", "type": "STRING" },
  { "name": "business_target", "type": "STRING" },
  { "name": "business_phase", "type": "STRING" },
  { "name": "business_model", "type": "STRING" },
  { "name": "city", "type": "STRING" },
  { "name": "uf", "type": "STRING" },
  { "name": "is_active", "type": "STRING" },
  { "name": "segment_primary", "type": "STRING" },
  { "name": "segment_secondary", "type": "STRING" },
  { "name": "tags", "type": "STRING" },
  { "name": "badges", "type": "STRING" }
]

crawler_schema = [
  { "name": "enrollments", "type": "INTEGER" },
  { "name": "inep", "type": "STRING" },
  { "name": "name", "type": "STRING" },
  { "name": "domain", "type": "STRING" },
  { "name": "homepage", "type": "STRING" },
  { "name": "facebook", "type": "STRING" },
  { "name": "instagram", "type": "STRING" },
  { "name": "email", "type": "STRING", "mode": "REPEATED" },
  { "name": "state", "type": "STRING" },
  { "name": "city", "type": "STRING" },
  { "name": "phone", "type": "STRING", "mode": "REPEATED" },
  { "name": "email_provider", "type": "STRING", "mode": "REPEATED" },
  { "name": "extracurricular", "type": "STRING", "mode": "REPEATED" },
  { "name": "all_tools", "type": "STRING", "mode": "REPEATED" },
  { "name": "administrative_management_system", "type": "STRING", "mode": "REPEATED" },
  { "name": "learning_management_system", "type": "STRING", "mode": "REPEATED" },
  { "name": "education_system", "type": "STRING", "mode": "REPEATED" },
  { "name": "bilingual_solution", "type": "STRING", "mode": "REPEATED" },
  { "name": "ecommerce", "type": "STRING", "mode": "REPEATED" },
  { "name": "communication", "type": "STRING", "mode": "REPEATED" },
  { "name": "edtech", "type": "STRING", "mode": "REPEATED" }
]