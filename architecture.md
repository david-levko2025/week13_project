``` mermaid
graph TD
    subgraph Root [black-coordinates-list]
        DC[docker-compose.yml]
        ENV[.env.example]
        RM[README.md]
        
        subgraph SA [service-a]
            REQ_A[requirements.txt]
            subgraph APP_A [app/]
                M_A[main.py]
                R_A[routes.py]
                S_A[services.py]
                SC_A[schemas.py]
                D_A[Dockerfile]
            end
        end

        subgraph SB [service-b]
            REQ_B[requirements.txt]
            subgraph APP_B [app/]
                M_B[main.py]
                R_B[routes.py]
                ST_B[storage.py]
                SC_B[schemas.py]
                D_B[Dockerfile]
            end
        end
    end

    %% קשרים בתוך Service A
    M_A --> R_A
    R_A --> S_A
    S_A -.-> SC_A
    R_A -.-> SC_A
    D_A --> APP_A

    %% קשרים בתוך Service B
    M_B --> R_B
    R_B --> ST_B
    ST_B -.-> SC_B
    R_B -.-> SC_B
    D_B --> APP_B

    %% קשרים ברמת ה-Infrastructure
    DC --> D_A
    DC --> D_B
    ENV -.-> SA
    ENV -.-> SB