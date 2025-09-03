import torch
import torch.nn as nn
import torch.optim as optim

class WorkflowClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(WorkflowClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        return self.fc2(out)

# Training loop
def train_model(X_train, y_train):
    model = WorkflowClassifier(input_size=X_train.shape[1], hidden_size=64, output_size=3)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(100):
        outputs = model(torch.tensor(X_train, dtype=torch.float32))
        loss = criterion(outputs, torch.tensor(y_train, dtype=torch.long))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    torch.save(model.state_dict(), "workflow_model.pt")
    return model
