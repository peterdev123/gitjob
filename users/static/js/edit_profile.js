$(document).ready(function(){
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

function distributeInWrapper(array, wrapper, div_name){
    if(Array.isArray(array)){
        array.forEach(function(item){
            const item_div = "<div class='"+div_name+"-div w-full m-0 mt-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
                + "<span class='align-middle'>" + item +"</span>"
                + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
                + "</div>"
            wrapper.append(item_div)
        })
    }else{
        console.log("Datatype of "+div_name+"_json: "+typeof(array))
    }
}
function addInWrapper(input_val, wrapper, div_name){
    if(input_val){
        const item = "<div class='"+div_name+"-div w-full m-0 mt-2 p-2 rounded-2xl flex items-center justify-between bg-green-200 border-2 border-black border-solid box-border'>"
            + "<span class='align-middle'>" + input_val +"</span>"
            + "<button onclick='deleteItem(this)' class='w-12 h-8 ml-4 rounded-2xl border-2 border-black border-solid bg-white text-red-600 text-sm'>Delete</button>"
            + "</div>"
        wrapper.append(item)
    }
}

function initEditSkills(){
    const skills = JSON.parse(document.getElementById("skills").textContent);
    const skill_wrapper = $("#skill_wrapper")
    skill_wrapper.html("")
    distributeInWrapper(skills, skill_wrapper, "skill")
}

function addSkill(){
    const input = $("#add_skill")
    const input_val = input.val()
    input.html("")
    addInWrapper(input_val, $("#skill_wrapper"), "skill")
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

function initEditExperiences(){
    const experiences = JSON.parse(document.getElementById("experiences").textContent);
    const exp_wrapper = $("#experience_wrapper")
    exp_wrapper.html("")
    distributeInWrapper(experiences, exp_wrapper, "experience")
}

function addExperience(){
    const input = $("#add_experience");
    const input_val = input.val()

    addInWrapper(input_val, $("#experience_wrapper"), "experience")
    input.html("")

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