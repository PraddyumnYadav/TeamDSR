from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def class9(request):
    notes = {
        "notes": [
            {
                "name": "The French Revolution",
                "pdf": "PDFs/Class 9th/The French Revolution one shot revision.pdf",
                "thumbnail": "Images/class9/the_french_revolution.webp",
            },
            {
                "name": "India - Size and Location",
                "pdf": "PDFs/Class 9th/India Size and Location one short revision.pdf",
                "thumbnail": "Images/class9/india_size_and_location.webp",
            },
            {
                "name": "What is Democracy? Why Democracy?",
                "pdf": "PDFs/Class 9th/what is democracy why democracy.pdf",
                "thumbnail": "Images/class9/what_democracy_why_democracy.webp",
            },
            {
                "name": "The Story of Village Palampur",
                "pdf": "PDFs/Class 9th/The story of village Palampur one shot revision series-1.pdf",
                "thumbnail": "Images/class9/story_of_village_palampur.webp",
            },
            {
                "name": "Socialism in Europe and the Russian Revolution",
                "pdf": "PDFs/Class 9th/Socialism in Europe and the Russian Revolution one shot.pdf",
                "thumbnail": "Images/class9/socialism_in_europe.webp",
            },
            {
                "name": "Physical Features of India",
                "pdf": "PDFs/Class 9th/Physical Features of India one shot.pdf",
                "thumbnail": "Images/class9/physical_features_of_india.webp",
            },
            {
                "name": "Constitutional Design",
                "pdf": "PDFs/Class 9th/Constitutional Design one shot.pdf",
                "thumbnail": "Images/class9/constituitional_design.webp",
            },
            {
                "name": "People as Resource",
                "pdf": "PDFs/Class 9th/People as Resource one shot.pdf",
                "thumbnail": "Images/class9/people_as_resource.webp",
            },
            {
                "name": "Electoral Politics",
                "pdf": "PDFs/Class 9th/Electoral politics one shot.pdf",
                "thumbnail": "Images/class9/electoral_politics.webp",
            },
            {
                "name": "Drainage",
                "pdf": "PDFs/Class 9th/Drainage one shot.pdf",
                "thumbnail": "Images/class9/drainage.webp",
            },
            {
                "name": "Half Yearly Map Work",
                "pdf": "PDFs/Class 9th/class 9 Half Yearly Exam Map Work.pdf",
                "thumbnail": "Images/class9/half_yearly_map_work.webp",
            },
            {
                "name": "Nazism and the Rise of Hitler",
                "pdf": "PDFs/Class 9th/Nazism and the Rise of Hitler one short.pdf",
                "thumbnail": "Images/class9/nazism_and_rise_of_hitler.webp",
            },
            {
                "name": "Nazism and the Rise of Hitler Poll Session",
                "pdf": "PDFs/Class 9th/Nazism and the Rise of Hitler poll session.pdf",
                "thumbnail": "Images/class9/nazism_and_rise_of_hitler_poll.webp",
            },
            {
                "name": "Poverty as a Challenge",
                "pdf": "PDFs/Class 9th/Poverty as a Challenge.pdf",
                "thumbnail": "Images/class9/poverty_as_a_challenge.webp",
            },
        ]
    }
    return render(request, "class9.html", context=notes)


def class10(request):
    return render(request, "class10.html")
