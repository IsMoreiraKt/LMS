# TODO: Lead Distribution Automation
## 1. Setting up a new Git repository
- [x] Environment Configuration
- [ ] Install Flask and VueJS

## 2. Backend
- [ ] Create a backend server with Flask
    - [ ] Configure Flask-CORS for API access
- Set up a database PostgreSQL
    - [ ] Create a leads table with fields: id, name, email, phone, status, assigned_to, created_at
- [ ] Implement a route to receive leads via webhook
    - [ ] Route: POST /api/leads
- [ ] Create a function to check if the lead already exists in the NoCRM.io database
    - [ ] Use the NoCRM.io API to query existing leads
- [ ] Implement lead distribution logic
- [ ] If the lead exists, assign to the salesperson responsible
    - [ ] If the lead does not exist, assign to the next available salesperson
- [ ] Return appropriate responses for success/failure

## 3. Frontend
- [ ] Create an interface with Vue.js
    - **Required Pages**
        - [ ] Home Page
        - [ ] Leads Insertion Page
            - [ ] Form to add a new lead
        - [ ] Leads visualisation page
            - [ ] Table/list showing all leads
        - [ ] Lead details page
        - [ ] Reports/Analyses page
        - [ ] Settings Page (Optional)
        - [ ] Login Page (Optional)
    - **Required Components**
        - [ ] Navbar
        - [ ] Footer
        - [ ] Lead Form
        - [ ] Lead Table
        - [ ] Notifications
        - [ ] Confirmation Modal
        - [ ] Analysis Charts
- [ ] Implement logic to send leads to the backend via API
- [ ] Stylise the interface to be friendly and responsive

## 4. Tests
- [ ] Create automated tests to check the verification and distribution logic
- [ ] Simulate different lead scenarios

## 5. Documentation
- [ ] Document the development process
- [ ] Create a README explaining how to use the application and requirements
    - [ ] Include API documentation
    - [ ] Setup instructions for development and deployment

## 6. Implementation and Final Tests
- [ ] Test the complete flow of the application
- [ ] Fix bugs and make adjustments as necessary
- [ ] Perform user acceptance testing