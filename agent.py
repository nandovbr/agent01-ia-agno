from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    id="agente_de_copy_corretor",
    name="Pesquisador",
    role="Responda com título e descrição sobre planos de saúde para anúncios pagos no facebook e Instagram",
    instructions=[
        "Busque as principais fontes confiáveis sobre o tema.",
        "Entregue uma saída concisa com: 2-5 fatos em bullets e um quadro de fontes com título.",
        "Não invente nada. Priorize sites e artigos oficiais e referências de boa qualidade.",
        "Use o ValyuTools para buscar em artigos e o DuckDuckGoTools para buscar na internet."
    ],
    model=Gemini(
        id="gemini-2.0-flash",
        vertexai=True,
        project_id="agente_de_copy_corretor",
        location="us-central1",
    ),
)

print(agent.print_response("plano de saúde sa UNIMED"))