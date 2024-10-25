$(document).ready(function(){
    initEditSkills();
    initEditExperiences();
    function showEditProfileModal() {
        $("#edit_profile_modal").show()
    }
    function hideEditProfileModal() {
        $("#edit_profile_modal").hide()
    }
    $("#edit_profile_btn").click(()=>{showEditProfileModal()})
    $("#edit_profile_cancel").click(()=>{hideEditProfileModal()})
    $("#edit_profile_exit").click(()=>{hideEditProfileModal()})

    function showAddSkillModal(){
        initEditSkills()
        updateSkills()
        $("#edit_skills_modal").show()
    }
    function hideAddSkillModal(){
        $("#edit_skills_modal").hide()
    }

    $("#edit_skills_btn").click(()=>{showAddSkillModal()})
    $("#edit_skills_cancel").click(()=>{hideAddSkillModal()})
    $("#edit_skills_exit").click(()=>{hideAddSkillModal()})

    function showAddExperienceModal(){
        initEditExperiences()
        updateExperiences()
        $("#edit_experiences_modal").show()
    }
    function hideAddExperienceModal(){
        $("#edit_experiences_modal").hide()
    }
    $("#edit_experiences_btn").click(()=>{showAddExperienceModal()})
    $("#edit_experiences_cancel").click(()=>{hideAddExperienceModal()})
    $("#edit_experiences_exit").click(()=>{hideAddExperienceModal()})

    $("#profile-pic").click(()=>{ $("#profile-pic-input").click() })
    $("#profile-pic-input").change(function() { this.form.submit() })
    $("input[type='file']").change(function() { this.form.submit() })
    $("#delete_resume_btn").click((event)=>{
        $(event.currentTarget).parent().submit();
    })
})

function deleteItem(element){
    const div = $(element).parent()
    div.remove()

    updateSkills()
    updateExperiences()
}

function initEditSkills(skills){
    const skill_wrapper = $("#skill_wrapper")
    skill_wrapper.html("")
    if(Array.isArray(skills)){
        skills.forEach(function(skill){
            const item = "<div class='skill-div w-full m-0 mb-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
                + "<span class='align-middle'>" + skill +"</span>"
                + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
                + "</div>"
            skill_wrapper.append(item)
        })
    }
}

function addSkill(){
    const input = $("#add_skill")
    const inputVal = input.val()

    if(inputVal){
        const itemWrapper = $("#skill_wrapper")
        const item = "<div class='skill-div w-full m-0 mb-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
            + "<span class='align-middle'>" + inputVal +"</span>"
            + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
            + "</div>"
        input.val("")
        itemWrapper.append(item)
    }

    updateSkills()
}

function updateSkills(){
    const skills = []

    $("#skill_wrapper .skill-div").each(function() {
        const skillText = $(this).find("span").text();
        skills.push(skillText);
    });

    const skillsJson = JSON.stringify(skills)

    $("#skills_json").val(skillsJson)
}

function initEditExperiences(experiences){
    const exp_wrapper = $("#experience_wrapper")
    exp_wrapper.html("")
    if(Array.isArray(experiences)){
        experiences.forEach(function(experience){
            const item = "<div class='experience-div w-full m-0 mb-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
                + "<span class='align-middle'>" + experience +"</span>"
                + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
                + "</div>"
                exp_wrapper.append(item)
        })
    }
}

function addExperience(){
    const input = $("#add_experience");
    const inputVal = input.val()

    if(inputVal){
        const itemWrapper = $("#experience_wrapper")
        const item = "<div class='experience-div w-full m-0 mb-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
            + "<span class='align-middle'>" + inputVal +"</span>"
            + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
            + "</div>"
        input.val("")
        itemWrapper.append(item)
    }

    updateExperiences()
}

function updateExperiences(){
    const experiences = []

    $("#experience_wrapper .experience-div").each(function() {
        const experienceText = $(this).find("span").text();
        experiences.push(experienceText);
    });

    const experiencesJson = JSON.stringify(experiences);

    $("#experiences_json").val(experiencesJson);
}